from timeit import default_timer as timer
from collections import OrderedDict
from typing import Tuple
import pandas as pd
import numpy as np
from scipy import optimize
from SAInT.normalization import MeanStdNormalizer, MinMaxNormalizer, NormalizationMeanStdValues, NormalizationMinMaxValues
from .common import denormalize_features, denormalize_outputs, normalize_features, normalize_outputs

def convert_to_list(self, values):
        """Ensure values are in list format."""
        return values if isinstance(values, list) else list(values)

class Optimizer():

    def __init__(self, dataloader, model, example, verbose: bool = False):
        self.dataloader = dataloader
        self.model = model
        self.verbose = verbose
        self.example = example
        self.normalizer = self._init_normalizer()

        # Update: remove invalid -1,-1 bounds
        self.manipulatable_features_dict_denormalized = self._get_valid_manipulatable_features()
        self.manipulatable_features_dict_normalized = self._normalize_features(self.manipulatable_features_dict_denormalized)
        self.x_bounds_dict = {}

    ################################ HELPER FUNCTIONS ################################

    def _init_normalizer(self):
        """Initialize the normalizer based on example's normalization type."""
        if self.example.normalization == "none":
            return None

        normalization_values = self.dataloader.train.get_normalization_values()
        if isinstance(normalization_values, NormalizationMinMaxValues):
            return MinMaxNormalizer(normalization_values=normalization_values, verbose=self.verbose)
        elif isinstance(normalization_values, NormalizationMeanStdValues):
            return MeanStdNormalizer(normalization_values=normalization_values, verbose=self.verbose)
        else:
            raise RuntimeError("Unsupported Normalization Type!")

    def _get_valid_manipulatable_features(self):
        """Filter out manipulatable features with invalid bounds (-1, -1)."""
        manipulatable_features_dict = self.example.get_manipulatable_features()
        return {m_name: (min_v, max_v, weight) for m_name, (min_v, max_v, weight) in manipulatable_features_dict.items()
                if min_v != -1.0 and max_v != -1.0}

    def _normalize_features(self, features_dict):
        """Normalize the feature values if required."""
        if self.example.normalization == "none":
            #eturn features_dict
            return {feature: convert_to_list(values) for feature, values in features_dict.items()}
        return normalize_features(self.dataloader, features_dict, do_convert=True)

    def _denormalize_features(self, features):
        """Denormalize the feature values if required."""
        if self.example.normalization == "none":
            #return features
            return {feature: convert_to_list(values) for feature, values in features.items()}
        return denormalize_features(self.dataloader, features, do_convert=True)

    def _normalize_output(self, output):
        """Normalize the output if normalization is enabled."""
        if self.example.normalization == "none":
            #return output
            return {feature: convert_to_list(values) for feature, values in output.items()}
        return normalize_outputs(self.dataloader, output, do_convert=True)

    def _denormalize_output(self, output):
        """Denormalize the output if normalization is enabled."""
        if self.example.normalization == "none":
            #return output
            return {feature: convert_to_list(values) for feature, values in output.items()}
        return denormalize_outputs(self.dataloader, output, do_convert=True)

    ################################ MODEL PREDICTION FUNCTIONS ##############################

    def _prepare_input_for_modelprediction(self, input):
        if isinstance(input, pd.DataFrame):
            input = input.values
        if isinstance(input, list):
            input = np.array(input)
        input = input.reshape(1, -1)
        return input

    def _get_output_for_input(self, input):
        """Prepare input and get model output."""
        input = self._prepare_input_for_modelprediction(input)
        return self.model.get_output(input).flatten()

    def _predict_and_denormalize(self, x):
        """Predict using model and denormalize the output."""
        pred = self._get_output_for_input(x)
        return self._denormalize_output(pred)

    def _predict_and_denormalize_optimized(self, optimized_x):
        """Predict and denormalize the optimized feature values."""
        new_pred = self._get_output_for_input(optimized_x)
        return self._denormalize_output(new_pred)

    ################################ OPTIMIZATION FUNCTIONS ##############################

    def _get_adaptations(self, original_values, optimized_values, epsilon: float = 1e-12):
        differences = optimized_values - original_values
        adaptations = {feature: diff_values.values[0] for feature, diff_values in differences.items()}
        return {feature: value for feature, value in adaptations.items() if abs(value) > epsilon}

    def _round_adaptations(self, adaptations, num_digits_rounding):
        if num_digits_rounding > 0:
            return {feature: round(adaptation, num_digits_rounding) for feature, adaptation in adaptations.items()}
        return adaptations

    def _apply_adaptations(self, org_x, adaptations) -> dict:
        """Apply adaptations to original x."""
        updated_x = org_x.copy()
        for feature, adaptation in adaptations.items():
            updated_x[feature] += adaptation
        return updated_x

    def _print_verbose_output(self, org_pred_denormalized, new_pred_denormalized, adaptations_denormalized_rounded):
        print("\nPrediction vs. new prediction:")
        print(self.example.get_quality_str(org_pred_denormalized))
        print(self.example.get_quality_str(new_pred_denormalized))
        print(f"\nAdvice for adaptation ({len(adaptations_denormalized_rounded)} features): \n")
        for feature, adaptation in adaptations_denormalized_rounded.items():
            print(f"{feature}: {adaptation}")

    def _extract_feature_names(self):
        feature_names = self.dataloader.train.inputs.columns
        return feature_names

    def _check_org_x(self, org_x):
        if org_x.empty:
            raise RuntimeError("optimization_advice Error: Original x is empty!")

    def _get_bounds_dict(self, org_x, feature_names):
        x_bounds_dict = self.get_bounds(org_x=org_x,
                                        feature_names=feature_names)
        return x_bounds_dict

    def _is_org_x_within_bounds(self, x_values, epsilon):
        return self.is_within_bounds(x_values=x_values, epsilon=epsilon)
    
    def _is_updated_x_within_bounds(self, updated_x, epsilon):
        return self.is_within_bounds(x_values=updated_x, epsilon=epsilon)

    def _get_bounds_for_optimization(self,
                                    delta_frac: float = 0.05,
                                    epsilon: float = 1e-12) -> tuple:
        x_bounds_list = []
        for x_min, x_max in self.x_bounds_dict.values():
            if x_min < x_max:
                delta = delta_frac * (x_max - x_min)
                x_min, x_max = x_min + delta, x_max - delta
            else:
                x_min, x_max = x_min - epsilon, x_max + epsilon
            x_bounds_list.append([x_min, x_max])
        return tuple(x_bounds_list)
    
    def _get_constraints(self, x_0, max_num_adaptations, epsilon):
        constraints = self.example.get_constraints(x_0=x_0,
                                                max_num_adaptations=max_num_adaptations,
                                                epsilon=epsilon)
        return constraints

    def _predict_output_normalized(self, updated_x_normalized):
        updated_pred = self._get_output_for_input(updated_x_normalized)
        return updated_pred

    def _perform_optimization(self, org_x, method, x_bounds_tuple, constraints, epsilon, step_size):
        org_x = self._prepare_input_for_modelprediction(org_x).flatten()
        results = optimize.minimize(fun=self._evaluate_model,
                                    x0=org_x,
                                    method=method,
                                    bounds=x_bounds_tuple,
                                    constraints=constraints,
                                    options={
                                         'disp': None,
                                         'eps': step_size,
                                         'maxiter': 5000,
                                         'ftol': epsilon
                                     })
        return results

    ################################ PUBLIC FUNCTIONS ##############################

    def get_bounds(self, org_x, feature_names: list) -> OrderedDict:
        x_bounds = OrderedDict()
        for feature in feature_names:
            if feature in self.manipulatable_features_dict_normalized.keys():
                x_min, x_max, weight = self.manipulatable_features_dict_normalized[
                    feature]
            else:
                # not manipulatable -> almost fix the bounds
                if isinstance(org_x, dict):
                    org_val = org_x[feature][0]
                elif isinstance(org_x, pd.DataFrame):
                    org_val = org_x[feature].values[0]
                else:
                    raise RuntimeError(
                        f"org_x: unsupported type {type(org_x)}!")
                x_min, x_max = org_val, org_val
            x_bounds[feature] = (x_min, x_max)
        return x_bounds
    
    def is_within_bounds(self, x_values, epsilon: float = 1e-12) -> bool:
        if isinstance(x_values, dict):
            extract_value = lambda feature: x_values[feature][0]
        elif isinstance(x_values, pd.DataFrame):
            extract_value = lambda feature: x_values[feature].values[0]
        elif isinstance(x_values, np.ndarray):
            extract_value = lambda feature, idx: x_values.flatten()[idx]
        else:
            raise RuntimeError(f"x: unsupported type {type(x_values)}!")

        for idx, (feature,
                  (min_value,
                   max_value)) in enumerate(self.x_bounds_dict.items()):
            value = extract_value(feature, idx) if isinstance(x_values, np.ndarray) \
                else extract_value(feature)

            if value + epsilon < min_value:
                if self.verbose:
                    print(f"{feature} out of bounds: {value} < {min_value}")
                return False
            if value - epsilon > max_value:
                if self.verbose:
                    print(f"{feature} out of bounds: {value} > {max_value}")
                return False
        return True

    def optimization_advice(self, org_x, bounds_delta_frac: float = 0.0, max_num_adaptations: int = -1,
                            num_digits_rounding: int = -1, step_size: float = 1e-1, epsilon: float = 1e-12, 
                            verbose: bool = True) -> Tuple[dict, str, float]:
        feature_names = self._extract_feature_names()

        self._check_org_x(org_x)

        org_pred_denormalized = self._predict_and_denormalize(x=org_x)
        self.x_bounds_dict = self._get_bounds_dict(org_x, feature_names)
        self._is_org_x_within_bounds(org_x, epsilon)

        x_bounds_tuple = self._get_bounds_for_optimization(bounds_delta_frac, epsilon)
        constraints = self._get_constraints(org_x, max_num_adaptations, epsilon)

        start = timer()
        method = "SLSQP"
        results = self._perform_optimization(org_x, method, x_bounds_tuple, constraints, epsilon, step_size)
        elapsed = timer() - start
        print(f"\nOptimization took {(elapsed):.3f} seconds.\n")

        if not results.success:
            return None, "Optimization did not work!", elapsed

        optimized_x = results.x

        if not self.is_within_bounds(x_values=optimized_x, epsilon=epsilon):
            return None, "results.x is NOT within bounds.", elapsed

        new_pred_denormalized = self._predict_and_denormalize_optimized(optimized_x)
        adaptations_normalized = self._get_adaptations(org_x, optimized_x, epsilon)

        updated_x = self._apply_adaptations(org_x, adaptations_normalized)
        self._is_updated_x_within_bounds(updated_x, epsilon)

        org_x_denormalized = self._denormalize_features(org_x)
        updated_x_denormalized = self._denormalize_features(updated_x)

        adaptations_denormalized = self._denormalize_features(adaptations_normalized)
        adaptations_denormalized_rounded = self._round_adaptations(adaptations_denormalized, num_digits_rounding)

        self._print_verbose_output(org_pred_denormalized, new_pred_denormalized, adaptations_denormalized_rounded)

        return adaptations_denormalized_rounded, "", elapsed

    def apply_denormalized_advice(self, org_x_denormalized, selected_adaptations_denormalized: dict) -> Tuple[dict, list]:
        selected_adaptations_denormalized_nonzero = {feature: adaptation for feature, adaptation in selected_adaptations_denormalized.items() if adaptation != 0.0}

        updated_x_denormalized = self._apply_adaptations(org_x_denormalized, selected_adaptations_denormalized_nonzero)
        updated_x_normalized = self._normalize_features(updated_x_denormalized)

        updated_pred = self._predict_output_normalized(updated_x_normalized)
        updated_pred_denormalized = self._denormalize_output(updated_pred)

        return updated_x_denormalized, updated_pred_denormalized

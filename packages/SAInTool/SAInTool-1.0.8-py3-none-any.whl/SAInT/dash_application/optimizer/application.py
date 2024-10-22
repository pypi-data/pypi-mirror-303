import random
from dash import html, callback_context
import numpy as np
import pandas as pd
import dash_bootstrap_components as dbc
from .common import denormalize_features, denormalize_outputs, normalize_features
from .optimizer import Optimizer
from .distribution_plot import DistributionPlot
from .sample_data import SampleData
from SAInT.dash_application.components import DashSlider, DashSliderGrid, DashSpinner, DashGraph

def get_pressed_buttons():
    changed_id = [p["prop_id"] for p in callback_context.triggered][0]
    return changed_id

class OptimizationApplication():

    def __init__(self,
                 dataloader,
                 mode,
                 optimizer: Optimizer,
                 num_digits_rounding: int = 2):
        self.dataloader = dataloader
        self.valid_samples_indices = None
        self.optimizer = optimizer
        self.num_digits_rounding = num_digits_rounding
        self.sample_data = None
        self.proposed_adaptations_denormalized = None
        self.selected_adaptations = {}
        self.distribution_plot = None
        self.sliders = None
        self.triggered_load = None
        self.div_content = ""
        self.pixel_definitions = None
        self.max_num_adaptations = -1

        # default: TEST dataset, fallback: VALID dataset
        if mode == "test":
            self.data = self.dataloader.to_test
        if mode == "valid":
            self.data = self.dataloader.to_valid
        if mode == "train":
            raise RuntimeError("train not yet supported")

        num_samples = len(self.data)
        if num_samples == 0:
            self.data = self.dataloader.to_valid
            num_samples = len(self.data)
            print("num_samples: ", num_samples)
            if num_samples == 0:
                raise RuntimeError("No samples in data!")

        # create x and y values for plots
        x_values = list(range(num_samples))

        num_outputs = len(dataloader.train.output_names)

        # load normalized groundtruth
        all_test_gt_normalized = [
            self.data.ys.values[i:i + 1][0][:] for i in range(num_samples)
        ]

        # denormalize groundtruth
        do_convert = self.optimizer.example.normalization != "none"
        all_test_gt_denormalized = [
            denormalize_outputs(dataloader, all_test_gt_normalized[i],
                                do_convert=do_convert)
            for i in range(num_samples)
        ]
        all_test_gt_denormalized = np.array(all_test_gt_denormalized).reshape(
            num_samples, -1)

        # sorting
        y_values_sorted = [
            sorted(all_test_gt_denormalized[:, i]) for i in range(num_outputs)
        ]

        # create valid samples indices
        feature_names = self.dataloader.train.inputs.columns
        valid_sample_indices = []
        opt_verbose = self.optimizer.verbose
        self.optimizer.verbose = False

        for sample_idx in range(num_samples):
            org_x_normalized = self.data.xs.iloc[sample_idx:sample_idx + 1]
            self.optimizer.x_bounds_dict = self.optimizer.get_bounds(
                org_x=org_x_normalized, feature_names=feature_names)
            if self.optimizer.is_within_bounds(x_values=org_x_normalized,
                                               epsilon=1e-12):
                valid_sample_indices.append(sample_idx)
        self.valid_samples_indices = valid_sample_indices
        print(self.valid_samples_indices)

        self.optimizer.verbose = opt_verbose

        example = self.optimizer.example
        criterion_thresholds = example.min_thresholds | example.max_thresholds
        self.distribution_plot = DistributionPlot(
            x_values=x_values,
            y_values_sorted=y_values_sorted,
            output_names=self.dataloader.train.output_names,
            num_rows=len(example.y_limits),
            num_cols=1,
            y_limits=example.y_limits,
            criterion_thresholds=criterion_thresholds)
        self.distribution_plot.create_figure()

    def get_random_sample_idx(self):
        rand_idx = random.randint(0, len(self.valid_samples_indices) - 1)
        sample_idx = self.valid_samples_indices[rand_idx]
        return sample_idx

    def load_sample(self, index: int):
        print(f"Select sample {index}\n")
        org_x_normalized = self.data.xs.iloc[index:index + 1]
        do_convert = self.optimizer.example.normalization != "none"
        org_x_denormalized = denormalize_features(self.dataloader, org_x_normalized,
                                                  do_convert=do_convert)
        org_gt_normalized = self.data.ys.iloc[index:index + 1]
        org_gt_denormalized = denormalize_features(self.dataloader, org_gt_normalized,
                                                   do_convert=do_convert)
        self.sample_data = SampleData(
            example=self.optimizer.example,
            sample_index=index,
            org_x_normalized=org_x_normalized,
            org_x_denormalized=org_x_denormalized,
            org_gt_normalized=org_gt_normalized,
            org_gt_denormalized=org_gt_denormalized,
            num_digits_rounding=self.num_digits_rounding)

        _, org_pred_denormalized = self.apply_adaptations(
            org_x_denormalized=org_x_denormalized, adaptations={})
        self.sample_data.org_pred_denormalized = org_pred_denormalized

        print(f"Optimize sample {self.sample_data.sample_index}\n")
    def optimize_sample(self, max_num_adaptations: int = -1) -> bool:
        if max_num_adaptations == -1:
            epsilon = 1e-12
        else:
            if max_num_adaptations > 15:
                epsilon=1e-3
            else:
                epsilon=1e-1
        success = False
        proposed_adaptations_denormalized, error_msg, time_elapsed = self.optimizer.optimization_advice(
            org_x=self.sample_data.org_x_normalized,
            num_digits_rounding=self.num_digits_rounding,
            bounds_delta_frac=0.05,
            step_size=1e-2,
            max_num_adaptations=max_num_adaptations,
            epsilon=epsilon)
        if error_msg == "":
            self.proposed_adaptations_denormalized = proposed_adaptations_denormalized
            success = True
        else:
            print(f"Optimization error: {error_msg}")
        return success

    def setup(self, dash_app, app, sample_idx: int) -> bool:
        self.pixel_definitions = app.application.pixel_definitions
        self.distribution_plot.reset_marker()
        self.load_sample(sample_idx)
        self.selected_adaptations = {
            feature: 0.0
            for feature in
            self.optimizer.manipulatable_features_dict_denormalized.keys()
            if feature in self.sample_data.org_x_denormalized.keys()
        }
        success = self.optimize_sample(max_num_adaptations=self.max_num_adaptations)
        if success:
            if self.sliders is None:
                self.create_sliders(dash_app, app)

            self.triggered_load = {
                feature: True
                for feature in self.selected_adaptations.keys()
            }
        else:
            print("Setup incomplete due to optimization error!")
        return success

    def apply_adaptations(self, org_x_denormalized, adaptations):
        target_x_denormalized, target_pred_denormalized = self.optimizer.apply_denormalized_advice(
            org_x_denormalized=org_x_denormalized,
            selected_adaptations_denormalized=adaptations)
        return target_x_denormalized, target_pred_denormalized

    def apply(self):
        target_x_denormalized, target_pred_denormalized = self.apply_adaptations(
            org_x_denormalized=self.sample_data.org_x_denormalized,
            adaptations=self.selected_adaptations)
        self.sample_data.adaptations_denormalized = self.selected_adaptations
        self.sample_data.target_x_denormalized = target_x_denormalized
        self.sample_data.target_pred_denormalized = target_pred_denormalized
        if len(self.distribution_plot.prediction_marker) == 2:
            self.distribution_plot.pop_oldest_marker()
        self.distribution_plot.add_marker(target_pred_denormalized)
        self.distribution_plot.plot()

    def create_marks(self, feature: str):
        original_value = self.sample_data.org_x_denormalized[feature]
        original_value = float(original_value)
        fontsize = self.pixel_definitions.text_font_size
        marks = {
            original_value: {
                "label": "original",
                "style": {"font-size": fontsize}
            }
        }
        if feature in self.proposed_adaptations_denormalized.keys():
            proposed_value = original_value + self.proposed_adaptations_denormalized[
                feature]
            proposed_value = float(proposed_value)
            marks[proposed_value] = {
                "label": "advice",
                "style": {"font-size": fontsize}
            }
        return marks

    ########################################################
    def get_proposed_adaptation_per_feature(self, feature):
        if feature in self.proposed_adaptations_denormalized.keys():
            return self.proposed_adaptations_denormalized[feature]
        return 0

    def get_org_pred_denormalized(self):
        return self.sample_data.org_pred_denormalized

    def get_org_x_denormalized(self):
        return self.sample_data.org_x_denormalized
    ########################################################

    def get_impact(self, relative_change: float):
        if relative_change < 1.0:
            impact = 1
        elif relative_change > 10.0:
            impact = 3
        else:
            impact = 2
        return impact

    def measure_impact_per_step(self,
                                feature,
                                original_value,
                                epsilon: float = 1e-7):

        proposed_adaptation = self.get_proposed_adaptation_per_feature(feature)
        org_x_denormalized = self.get_org_x_denormalized()

        _, pred_changed = self.apply_adaptations(
            org_x_denormalized=org_x_denormalized,
            adaptations={feature: proposed_adaptation})
        pred_org = self.get_org_pred_denormalized()

        absolute_change = sum(
            [abs(o - p) for o, p in zip(pred_org, pred_changed)])
        if original_value == 0.0:
            original_value += epsilon
        relative_change = (absolute_change / original_value) * 100.0

        impact = self.get_impact(relative_change)
        print(
            f"{feature}: {absolute_change:.3f} change ({relative_change:.3f} %) -> impact: {impact}"
        )
        return impact

    def create_sliders(self, dash_app, app):
        self.sliders = {}
        features = list(
            self.optimizer.manipulatable_features_dict_denormalized.keys())
        sliders = []
        for feature_index, feature in enumerate(features):
            if feature not in self.sample_data.org_x_denormalized.keys():
                continue
            min_value, max_value, weight = self.optimizer.manipulatable_features_dict_denormalized[
                feature]
            step = (max_value - min_value) / 100.0
            original_value = self.sample_data.org_x_denormalized[feature]
            marks = self.create_marks(feature)
            sliders.append({
                "label": f"{feature}",
                "id": {'type': 'slider', 'index': feature_index},
                "weight": weight,
                "min": min_value,
                "max": max_value,
                "step": step,
                "value": original_value,
                "marks": marks,
            })
        sorted_sliders = sorted(sliders,
                                key=lambda slider: slider['weight'],
                                reverse=False)

        checklist_text = {1: "low", 2: "medium", 3: "high"}
        pixel_def = self.pixel_definitions
        for slider in sorted_sliders:
            slider_text = f"effort: {checklist_text[slider['weight']]}"
            impact = self.measure_impact_per_step(
                feature=slider["label"], original_value=slider["value"])
            slider_text += f", impact: {checklist_text[impact]}"
            index = slider["id"]["index"]
            self.sliders[slider["label"]] = DashSlider(slider=slider,
                                                       slider_text=slider_text,
                                                       id={'type': 'slider-text', 'index': index}).to_html(pixel_def)

    def create_outputs(self) -> dict:
        outputs = {}
        output_data = {
            "load_output": self.sample_data.sample_info_text,
            "features_output": self.sample_data.target_feature_text,
            "prediction_output": self.sample_data.prediction_text,
            "adaptations_output": self.sample_data.adaptation_text,
            "groundtruth_output": self.sample_data.groundtruth_text
        }
        pixel_def = self.pixel_definitions
        for key, value in output_data.items():
            outputs[key] = DashSpinner(obj=dbc.FormText(children=value, id=key),
                                       id=f"loading-{key}").to_html(pixel_def)
        return outputs

    def get_optimized_features_to_all_samples(self) -> list:
        feature_names = self.dataloader.train.inputs.columns
        optimization_times_successful, optimization_times_error = [], []
        all_target_x_denormalized = []
        for i, sample_idx in enumerate(self.valid_samples_indices):

            if len(optimization_times_successful) > 0:
                print(
                    "\nAverage time of successful samples: " \
                   + f"{np.average(optimization_times_successful):.2f} s"
                )

            if len(optimization_times_error) > 0:
                print(
                    "\nAverage time of samples with optimization errors: " \
                    + f"{np.average(optimization_times_error):.2f} s"
                )

            print(
                f"\nSelect test sample {sample_idx} ({i}/{len(self.valid_samples_indices)})\n"
            )

            org_x_normalized = self.data.xs.iloc[sample_idx:sample_idx + 1]
            self.optimizer.x_bounds_dict = self.optimizer.get_bounds(
                org_x=org_x_normalized, feature_names=feature_names)
            if not self.optimizer.is_within_bounds(x_values=org_x_normalized,
                                                   epsilon=1e-12):
                print(
                    self.optimizer.is_within_bounds(x_values=org_x_normalized,
                                                    epsilon=1e-12))
                raise RuntimeError(f"{sample_idx}: org x not within bounds!")

            do_convert = self.optimizer.example.normalization != "none"
            org_x_denormalized = denormalize_features(self.dataloader, org_x_normalized,
                                                      do_convert=do_convert)

            proposed_adaptations_denormalized, error_msg, time_elapsed = self.optimizer.optimization_advice(
                org_x=org_x_normalized,
                num_digits_rounding=self.num_digits_rounding,
                bounds_delta_frac=0.05,
                max_num_adaptations=-1,
                step_size=1e-1,
                epsilon=1e-12)

            if error_msg != "":
                print(f"{sample_idx}: no successful optimization!")
                optimization_times_error.append(time_elapsed)
                continue
            optimization_times_successful.append(time_elapsed)

            target_x_denormalized, _ = self.apply_adaptations(
                org_x_denormalized=org_x_denormalized,
                adaptations=proposed_adaptations_denormalized)

            do_convert = self.optimizer.example.normalization != "none"
            target_x_normalized = normalize_features(self.dataloader, target_x_denormalized,
                                                     do_convert=do_convert)

            target_x_normalized = pd.DataFrame(
                {k: [v]
                 for k, v in target_x_normalized.items()})
            if not self.optimizer.is_within_bounds(
                    x_values=target_x_normalized, epsilon=1e-12):
                raise RuntimeError(f"{sample_idx}: new x not within bounds!")

            all_target_x_denormalized.append(target_x_denormalized)

        return all_target_x_denormalized

    def write_samples_to_csv(self,
                             sample_features: list,
                             template: str = "template.xlsm") -> None:
        output_path = "optimized_samples.xlsm"
        self.optimizer.example.write_samples_to_csv(sample_features=sample_features,
                                                    template=template,
                                                    output_path=output_path)

    def create_output_container(self, outputs):
        return dbc.Container([
            dbc.Row([
                dbc.Col([html.H6("Sample Information"), outputs["load_output"]], width=2),
                dbc.Col([html.H6("Prediction"), outputs["prediction_output"]], width=5),
                dbc.Col([html.H6("Groundtruth"), outputs["groundtruth_output"]], width=5)
            ]),
            html.Br(),
            html.Br(),
            dbc.Row([html.H6("Adaptation"), outputs["adaptations_output"]]),
            html.Br(),
            html.Br(),
            dbc.Row([html.H6("Features"), outputs["features_output"]])
        ], style = {
                "width": "100%",
                "padding": "0px",
                "margin": "0px",
            }
        )

    def prepare(self, dash_app, app, sample_idx):
        self.pixel_definitions = app.application.pixel_definitions
        success = self.setup(dash_app, app, sample_idx=sample_idx)
        if not success:
            raise RuntimeError(f"Cannot optimize current sample with index {sample_idx}!")
        self.apply()
        outputs = self.create_outputs()
        dbc_outputs = self.create_output_container(outputs)
        pixel_def = self.pixel_definitions
        slider_grid = DashSliderGrid(sliders=self.sliders, id="sliders_container_grid", cols=6).to_html(pixel_def)
        graph = DashGraph(figure=self.distribution_plot.figure, id="optimizer_distribution_plot").to_html(pixel_def)
        dbc_graph = DashSpinner(obj=graph, id="loading-6").to_html(pixel_def)
        self.div_content = html.Div(
            id="content",
            children=[
                dbc.Container([
                    slider_grid,
                    dbc.Row([
                        dbc_outputs,
                        dbc_graph
                    ])
                ], fluid=True)
            ],
            style={
                "width": "100%",
                "padding": "0px",
                "margin": "0px",
            }
        )

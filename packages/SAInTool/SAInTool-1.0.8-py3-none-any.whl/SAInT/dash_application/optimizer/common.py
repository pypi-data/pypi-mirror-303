from typing import Tuple, Union, List
import pandas as pd
from SAInT.normalization import NormalizationMeanStdValues, NormalizationMinMaxValues

def is_min_max(dataloader):
    normalization_values = dataloader.train.get_normalization_values()
    if normalization_values is None:
        return False
    return isinstance(normalization_values, NormalizationMinMaxValues)

def get_normalization_vals(dataloader) -> Tuple[pd.Series, pd.Series]:
    normalization_values = dataloader.train.get_normalization_values()
    if isinstance(normalization_values, NormalizationMeanStdValues):
        return normalization_values.mean_values, normalization_values.std_values
    if isinstance(normalization_values, NormalizationMinMaxValues):
        return normalization_values.min_values, normalization_values.max_values
    return (None, None)

def normalize_mean_std(value: float, mean_v: float, std_v: float) -> float:
    return (value - mean_v) / std_v

def denormalize_mean_std(value: float, mean_v: float, std_v: float) -> float:
    return (value * std_v) + mean_v

def normalize_min_max(value: float, min_v: float, max_v: float) -> float:
    return (value - min_v) / (max_v - min_v)

def denormalize_min_max(value: float, min_v: float, max_v: float) -> float:
    return (value * (max_v - min_v)) + min_v

def process_values(values: Union[List, Tuple, float, int, pd.Series]):
    if isinstance(values, int):
        return [float(values)]
    if isinstance(values, float):
        return [values]
    return values

def apply_normalization(values: List[float], mean_v: float, std_v: float, func) -> List[float]:
    return [func(v, mean_v, std_v) for v in values]

def process_features(dataloader, input_feature_dict: dict, do_convert: bool, func) -> dict:
    result_features_dict = {}
    norm_values_1, norm_values_2 = get_normalization_vals(dataloader) if do_convert else (None, None)

    for feature_name, values in input_feature_dict.items():
        values = process_values(values)
        if do_convert:
            if feature_name not in norm_values_1:
                continue
            values_normalized = apply_normalization(values, norm_values_1[feature_name], norm_values_2[feature_name], func)
        else:
            values_normalized = list(values)

        result_features_dict[feature_name] = values_normalized[0] if len(values_normalized) == 1 else values_normalized

    return result_features_dict

def normalize_features(dataloader, input_feature_dict: dict, do_convert: bool) -> dict:
    func = normalize_min_max if is_min_max(dataloader) else normalize_mean_std
    return process_features(dataloader, input_feature_dict, do_convert, func)

def denormalize_features(dataloader, input_feature_dict: dict, do_convert: bool) -> dict:
    func = denormalize_min_max if is_min_max(dataloader) else denormalize_mean_std
    return process_features(dataloader, input_feature_dict, do_convert, func)

def denormalize_outputs(dataloader, output, do_convert: bool) -> List:
    output_names = dataloader.train.outputs.columns
    features_dict = {
        m_name: [out_val]
        for m_name, out_val in zip(output_names, output)
    }
    features_dict = denormalize_features(dataloader, features_dict, do_convert=do_convert)
    return list(features_dict.values())

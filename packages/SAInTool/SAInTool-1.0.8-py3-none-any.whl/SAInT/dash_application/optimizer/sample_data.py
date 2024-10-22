import pandas as pd


class SampleData:

    def __init__(
        self,
        example,
        sample_index: int,
        org_x_normalized: pd.DataFrame = None,
        org_x_denormalized: dict = None,
        org_gt_normalized: pd.DataFrame = None,
        org_gt_denormalized: dict = None,
        org_pred_denormalized: list = None,
        target_x_denormalized: dict = None,
        target_pred_denormalized: list = None,
        adaptations_denormalized: dict = None,
        num_digits_rounding: int = 2,
    ):
        self.sample_index = sample_index
        self.org_x_normalized = org_x_normalized
        self.org_x_denormalized = org_x_denormalized
        self.org_gt_normalized = org_gt_normalized
        self.org_gt_denormalized = org_gt_denormalized
        self.org_pred_denormalized = org_pred_denormalized
        self.target_x_denormalized = target_x_denormalized
        self.target_pred_denormalized = target_pred_denormalized
        self.adaptations_denormalized = adaptations_denormalized
        self.num_digits_rounding = num_digits_rounding
        self.example = example

    @property
    def sample_info_text(self) -> str:
        return self._get_sample_info_str(self.sample_index)

    @property
    def target_feature_text(self) -> str:
        return self._get_feature_str(self.target_x_denormalized)

    @property
    def prediction_text(self) -> str:
        return self._get_quality_str(self.target_pred_denormalized)

    @property
    def groundtruth_text(self) -> str:
        org_gt_denormalized_list = list(self.org_gt_denormalized.values())
        groundtruth_quality_str = self._get_quality_str(
            org_gt_denormalized_list)
        groundtruth_text = groundtruth_quality_str if sum(
            self.adaptations_denormalized.values(
            )) == 0.0 else "Groundtruth not available for adapted value."
        return groundtruth_text

    @property
    def adaptation_text(self) -> str:
        return self._get_adaptations_str(self.adaptations_denormalized)

    def _get_sample_info_str(self, index: int) -> str:
        return f"Sample {index}"

    def _format_dict_as_str(self, data: dict) -> str:
        return ", ".join([
            f"{key}: {value:.{self.num_digits_rounding}f}"
            for key, value in data.items() if value != 0.0
        ])

    def _get_feature_str(self, features: dict) -> str:
        return self._format_dict_as_str(features)

    def _get_adaptations_str(self, adaptations: dict) -> str:
        adaptation_text = self._format_dict_as_str(adaptations)
        return "No adaptation applied." if adaptation_text == "" else adaptation_text

    def _get_quality_str(self, outputs: list) -> str:
        return self.example.get_quality_str(outputs)

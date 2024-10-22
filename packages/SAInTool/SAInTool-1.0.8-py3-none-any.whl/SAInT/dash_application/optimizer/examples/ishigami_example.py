from collections import OrderedDict
from SAInT.dash_application.optimizer.example import Example
import json

class IshigamiExample(Example):
    def __init__(self, config_file: str, normalization: str):
        super().__init__()
        self.set_normalization(normalization)
        self.load_config(config_file)

    def load_config(self, config_file: str):
        with open(config_file, "r") as f:
            config = json.load(f)
        
        # Set manipulatable features
        self.set_manipulatable_features_dict(OrderedDict(config["manipulatable_features"]))

        # Apply limits, thresholds, and objectives
        for output_name, limits in config["limits"].items():
            self.add_limits(output_name, *limits)

        for output_name, min_threshold in config["min_thresholds"].items():
            self.add_min_threshold(output_name, min_threshold)

        for output_name, max_threshold in config["max_thresholds"].items():
            self.add_max_threshold(output_name, max_threshold)

        for obj in config["objectives"]["minimize"]:
            self.add_obj_minimize(obj)

        for obj in config["objectives"]["maximize"]:
            self.add_obj_maximize(obj)

        for output_name, equality_constraints in config["equality_constraints"].items():
            self.add_equality_constraint(*equality_constraints)

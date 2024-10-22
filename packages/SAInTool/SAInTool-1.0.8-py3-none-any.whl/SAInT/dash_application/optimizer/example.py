from collections import OrderedDict
import json

def get_max_adaptations_func(x_0_values, max_num_adaptations: int, epsilon: float = 1e-12):
    return lambda x_values: -((sum(int(abs(x_values[i] - x_0_values[i]) > epsilon)
                                   for i in range(len(x_0_values))) - max_num_adaptations) ** 2)

class Example:
    def __init__(self, config_file: str, output_names: list, normalization: str):
        self.manipulatable_features_dict = {}
        self.output_names = output_names
        self.y_limits = {}
        self.min_thresholds = {}
        self.max_thresholds = {}
        self.obj_maximize = []
        self.obj_minimize = []
        self.constraints = []
        self.start_sample_idx = 1
        self.normalization = normalization
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

    def get_constraints(self, x_0,
                    max_num_adaptations: int = -1,
                    epsilon: float = 1e-12) -> tuple:
        constraints = self.constraints
        if max_num_adaptations > -1:
            x_0_values = list(x_0.values.flatten())
            constraints.append({
                'type': 'ineq',
                'fun': get_max_adaptations_func(x_0_values, max_num_adaptations, epsilon)
            })
        return tuple(constraints)

    def set_manipulatable_features_dict(self, manipulatable_dict):
        self.manipulatable_features_dict = manipulatable_dict

    def get_manipulatable_features(self) -> dict:
        return self.manipulatable_features_dict

    def add_limits(self, name: str, lower: float, upper: float):
        self.y_limits[name] = (lower, upper)

    def add_min_threshold(self, name: str, value: float):
        self.min_thresholds[name] = value

    def add_max_threshold(self, name: str, value: float):
        self.max_thresholds[name] = value

    def set_normalization(self, method: str):
        self.normalization = method

    def add_equality_constraint(self, left_idx, right_idx):
        self.constraints.append({
            'type': 'eq',
            'fun': lambda x_values: x_values[left_idx] - x_values[right_idx]
        })

    def add_obj_maximize(self, name: str):
        self.obj_maximize.append(name)

    def add_obj_minimize(self, name: str):
        self.obj_minimize.append(name)

    def get_quality_str(self, output_denormalized: list) -> str:
        quality_str = "OK" if self.all_criterion_fulfilled(output_denormalized) else "not OK"
        output_str = ", ".join([str(o) for o in output_denormalized])
        return f"Output: {output_str} -> Product Quality: {quality_str}"

    def all_criterion_fulfilled(self, output_denormalized):
        for name, value in zip(self.output_names, output_denormalized):
            if name in self.min_thresholds:
                if not value > self.min_thresholds[name]:
                    return False
            if name in self.max_thresholds:
                if not value < self.max_thresholds[name]:
                    return False
        return True

    def eval_objective(self, pred):
        result = 0
        for name, value in zip(self.output_names, pred):
            if name in self.obj_maximize:
                result += value
            if name in self.obj_minimize:
                result -= value
        return -result

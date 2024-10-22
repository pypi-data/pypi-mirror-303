class Example:
    def __init__(self):
        self.y_limits = {}
        self.normalization = "none"
        self.manipulatable_features_dict = {}
        self.criterion_thresholds = {}
        self.start_sample_idx = 1
        self.constraints = []

    def get_constraints(self, x_0,
                    max_num_adaptations: int = -1,
                    epsilon: float = 1e-12) -> tuple:
        return tuple(self.constraints)

    def eval_objective(self, pred):
        raise NotImplementedError()

    def get_manipulatable_features(self) -> dict:
        return self.manipulatable_features_dict

    def add_limit(self, name: str, value: float):
        self.y_limits[name] = value

    def add_criterion_threshold(self, name: str, value: float):
        self.criterion_thresholds[name] = value

    def set_normalization(self, method: str):
        self.normalization = method

    def add_equality_constraint(self, left_idx, right_idx):
        self.constraints.append({
            'type': 'eq',
            'fun': lambda x_values: x_values[left_idx] - x_values[right_idx]
        })

    def add_max_adaptations_constraint(self,
                                       x_0,
                                       max_num_adaptations: int,
                                       epsilon: float = 1e-12):
        if max_num_adaptations > -1:
            x_0_values = list(x_0.values.flatten())  # Flatten x_0 as done in your example
            self.constraints.append({
                'type': 'ineq',
                'fun': lambda x_values: -(sum(int(abs(x_values[i] - x_0_values[i]) > epsilon)
                                            for i in range(len(x_0_values))) - max_num_adaptations)
            })

    def all_criterion_fulfilled(self, output_denormalized):
        # TODO
        #return False
        return True

    def get_quality(self, output_denormalized: list) -> float:
        if self.all_criterion_fulfilled(output_denormalized):
            return 1.0
        return 0.0

    def get_quality_str(self, output_denormalized: list) -> str:
        quality = self.get_quality(output_denormalized)
        quality_str = "OK" if quality == 1.0 else "not OK"
        return f"Product Quality: {quality_str}"

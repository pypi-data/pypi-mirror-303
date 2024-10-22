import os
from dash import html
from SAInT.dash_application.optimizer.application import OptimizationApplication
from SAInT.dash_application.optimizer.optimizer import Optimizer
from SAInT.dash_application.optimizer.example import Example


class DashOptimizer:
    def __init__(self, application):
        """
        Initialize the DashOptimizer instance.

        :param application: The application instance.
        """
        self.application = application
        self.hex_colors = application.color_palette.to_hex_list()
        self.decimal_colors = application.color_palette.to_decimal_list()
        self.optimizer = None
        self.example = None
        self.optimization_application = None
        self.do_save = True
        self.div_content = ""

    def reset(self):
        self.optimizer = None
        self.example = None
        self.optimization_application = None
        self.do_save = True
        self.div_content = ""

    def prepare(self, dash_app, app, sample_idx, ds_name):
        trainer = self.application.trainer
        if not trainer:
            return ""

        model = self.application.model_handler.best_model
        if not model:
            return ""

        if not self.example:
            data_settings = trainer.data_settings
            config_path = os.path.join(self.application.data_folder, "optimizer_config.json")
            if os.path.exists(config_path):
                self.example = Example(config_path, data_settings.output_names, data_settings.normalization)

        if not self.optimizer or self.application.model_handler.best_model_was_changed:
            if not self.example:
                return ""
            if not ds_name:
                raise RuntimeError("Dataset name is undefined!")

            self.optimizer = Optimizer(
                dataloader=trainer.dataloader,
                model=model,
                example=self.example,
                verbose=trainer.data_settings.verbose
            )

            self.optimization_application = OptimizationApplication(
                dataloader=trainer.dataloader,
                mode=ds_name,
                optimizer=self.optimizer,
                num_digits_rounding=2
            )

        if self.optimizer:
            self.optimization_application.prepare(dash_app, app, sample_idx)
            self.div_content = self.optimization_application.div_content
        else:
            self.div_content = ""

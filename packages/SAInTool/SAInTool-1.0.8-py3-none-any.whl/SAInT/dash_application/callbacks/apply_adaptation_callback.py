from dash import Input, Output
from SAInT.dash_application.common.dash_functions import get_pressed_buttons
from dash.exceptions import PreventUpdate

def register_apply_adaptation_callback(dash_app, app):
    @dash_app.callback(
        Output("load_output", "children"),
        Output("features_output", "children"),
        Output("adaptations_output", "children"),
        Output("prediction_output", "children"),
        Output("groundtruth_output", "children"),
        Output("optimizer_distribution_plot", "figure"),
        Input("apply_advice_button", "n_clicks"),
        prevent_initial_call=True
    )
    def apply_adaptation(n_clicks):
        optapp = app.application.optimizer.optimization_application
        changed_id = get_pressed_buttons()
        if "apply_advice_button.n_clicks" in changed_id:
            app.application.optimizer.optimization_application.apply()
        else:
            raise PreventUpdate
        return optapp.sample_data.sample_info_text, optapp.sample_data.target_feature_text, \
                optapp.sample_data.adaptation_text, optapp.sample_data.prediction_text, \
                optapp.sample_data.groundtruth_text, optapp.distribution_plot.figure

from dash import dcc, html, Input, Output, MATCH
from SAInT.dash_application.common.dash_functions import get_pressed_buttons

def register_slider_callbacks(dash_app, app):

    @dash_app.callback(
        Output({'type': 'slider', 'index': MATCH}, "value"),
        Output({'type': 'slider', 'index': MATCH}, "marks"),
        Output({'type': 'slider-text', 'index': MATCH}, "children"),
        Input({'type': 'slider', 'index': MATCH}, "value"),
        Input({'type': 'slider', 'index': MATCH}, "marks"),
        Input({'type': 'slider', 'index': MATCH}, "id"),
        Input("set_effort_checklist", "value"),
        Input("set_impact_checklist", "value"),
        Input("set_to_original_button", "n_clicks"),
        Input("set_to_advice_button", "n_clicks")
    )
    def update_slider(value: float, marks: dict, slider_id: dict,
                      set_effort_checklist, set_impact_checklist,
                      n_clicks_set_original: int,
                      n_clicks_set_advice: int
                      ):
        optapp = app.application.optimizer.optimization_application
        checklist_text = {1: "low", 2: "medium", 3: "high"}

        # Extract the feature index from the slider_id dictionary
        feature_idx = slider_id["index"]
        features = list(optapp.optimizer.manipulatable_features_dict_denormalized.keys())
        feature = features[feature_idx]

        changed_id = get_pressed_buttons()

        weight = optapp.optimizer.manipulatable_features_dict_denormalized[feature][2]
        original_value = optapp.sample_data.org_x_denormalized[feature]
        marks = optapp.create_marks(feature)

        weight_str = checklist_text[weight]
        slider_text = f"effort: {weight_str}"

        impact = optapp.measure_impact_per_step(feature, original_value)
        impact_str = checklist_text[impact]
        slider_text += f", impact: {impact_str}"

        if "set_to_original_button.n_clicks" in changed_id:
            if weight_str in set_effort_checklist and impact_str in set_impact_checklist:
                value = original_value
        elif "set_to_advice_button.n_clicks" in changed_id:
            if feature in optapp.proposed_adaptations_denormalized.keys():
                if weight_str in set_effort_checklist and impact_str in set_impact_checklist:
                    proposed_change = optapp.proposed_adaptations_denormalized[feature]
                    proposed_value = original_value + proposed_change
                    value = proposed_value
        elif optapp.triggered_load[feature]:
            value = original_value
            optapp.triggered_load[feature] = False

        optapp.selected_adaptations[feature] = value - original_value
        return value, marks, slider_text

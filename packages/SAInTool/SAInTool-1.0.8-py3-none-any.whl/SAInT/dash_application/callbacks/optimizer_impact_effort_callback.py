from dash import Input, Output
from SAInT.dash_application.common.dash_functions import get_pressed_buttons

def register_sync_effort_callback(dash_app, app):
    @dash_app.callback(
        Output("set_effort_checklist", "value"),
        Output("set_effort_all_checklist", "value"),
        Input("set_effort_checklist", "value"),
        Input("set_effort_checklist", "options"),
        Input("set_effort_all_checklist", "value"),
        prevent_initial_call=True
    )
    def update_effort_checklist(selected, checklist_options, all_selected):
        changed_id = get_pressed_buttons()
        if "set_effort_checklist" in changed_id:
            all_selected = [
                "all"
            ] if set(selected) == set(checklist_options) else []
        else:
            selected = checklist_options if all_selected else []
        return selected, all_selected

def register_sync_impact_callback(dash_app, app):
    @dash_app.callback(
        Output("set_impact_checklist", "value"),
        Output("set_impact_all_checklist", "value"),
        Input("set_impact_checklist", "value"),
        Input("set_impact_checklist", "options"),
        Input("set_impact_all_checklist", "value"),
        prevent_initial_call=True
    )
    def update_impact_checklist(selected, checklist_options, all_selected):
        changed_id = get_pressed_buttons()
        if "set_impact_checklist" in changed_id:
            all_selected = [
                "all"
            ] if set(selected) == set(checklist_options) else []
        else:
            selected = checklist_options if all_selected else []
        return selected, all_selected

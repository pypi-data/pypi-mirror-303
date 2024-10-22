from dash import Input, Output
from dash.exceptions import PreventUpdate
from SAInT.dash_application.common.dash_functions import get_pressed_buttons

def register_data_callback(dash_app, app):
    @dash_app.callback(
        Output("sort_criterion_radiobutton", "value"),
        Output("data_radiobutton", "options"),
        Output("data_radiobutton", "value"),
        Output("data_checklist", "options"),
        Output("data_checklist", "value"),
        Output("loss_radiobutton", "value"),
        Output("goodness_of_fit_radiobutton", "value"),
        Output("show_feature_details_radiobutton", "value"),
        Output("update_panel_from_settings", "children"),
        Output("loaded_data", "children"),
        Output("folder_path_info", "value"),
        Output("data-error-dialog", "displayed"),
        Output("data-error-dialog", "message"),
        Input("trigger_load_data_button", "n_clicks"),
        Input("trigger_load_data_after_feature_selection", "children"),
        prevent_initial_call=True
    )
    def update_data(trigger_load_data_button, trigger_load_data_after_feature_selection):
        return handle_data_update(app, trigger_load_data_button, trigger_load_data_after_feature_selection)

def handle_data_update(app, trigger_load_data_button, trigger_load_data_after_feature_selection):
    changed_id = get_pressed_buttons()

    # Check if neither button was pressed, prevent update
    if not is_data_load_triggered(changed_id):
        raise PreventUpdate

    # Initialize default values for UI components
    default_values = initialize_default_values()

    try:
        # Perform data loading if triggered by feature selection
        if "trigger_load_data_after_feature_selection" in changed_id:
            load_data(app)

        # Populate values based on application state if data exists
        if app.data_handler is not None and app.application is not None:
            update_ui_based_on_app_state(app, default_values)

    except RuntimeError as error:
        # Handle data loading error
        default_values["error_dialog_displayed"] = True
        default_values["error_dialog_message"] = str(error)

    return (
        default_values["sort_criterion_radiobutton_value"],
        default_values["data_radiobutton_options"],
        default_values["data_radiobutton_value"],
        default_values["data_checklist_options"],
        default_values["data_checklist_value"],
        default_values["loss_radiobutton_value"],
        default_values["goodness_of_fit_value"],
        default_values["show_feature_details_value"],
        default_values["update_panel_from_settings"],
        default_values["loaded_data"],
        default_values["folder_path_info"],
        default_values["error_dialog_displayed"],
        default_values["error_dialog_message"]
    )

def is_data_load_triggered(changed_id):
    """Check if data load was triggered by either button."""
    return "trigger_load_data_after_feature_selection" in changed_id or "trigger_load_data_button" in changed_id

def initialize_default_values():
    """Initialize default values for UI components."""
    return {
        "sort_criterion_radiobutton_value": "no sorting",
        "data_radiobutton_options": ["train", "valid", "test"],
        "data_radiobutton_value": "",
        "data_checklist_options": ["train", "valid", "test"],
        "data_checklist_value": [],
        "loss_radiobutton_value": "mae",
        "goodness_of_fit_value": "False",
        "show_feature_details_value": "False",
        "update_panel_from_settings": "False",
        "loaded_data": "False",
        "folder_path_info": "",
        "error_dialog_displayed": False,
        "error_dialog_message": ""
    }

def load_data(app):
    """Trigger the data loading process."""
    app.data_handler.load_data()

def update_ui_based_on_app_state(app, default_values):
    """Update the UI values based on the current application state."""
    trainer = app.application.trainer

    if trainer and trainer.data_settings:
        default_values["loss_radiobutton_value"] = trainer.data_settings.metric

    if trainer and trainer.dataloader:
        data_info = app.data_handler.get_data_info()
        dataset_dict = trainer.dataloader.datasets

        # Filter out datasets with no samples
        dataset_names = [mode for mode, dataset in dataset_dict.items() if dataset and dataset.num_samples > 0]
        default_values["data_radiobutton_options"] = dataset_names
        default_values["data_checklist_options"] = dataset_names
        default_values["update_panel_from_settings"] = "True"
        default_values["loaded_data"] = "True"
        default_values["folder_path_info"] = data_info

    # Set interactive plot-related UI states
    update_interactive_plot_ui(app, default_values)

def update_interactive_plot_ui(app, default_values):
    """Update UI values related to the interactive plot."""
    interactive_plot = app.application.interactive_plot
    if interactive_plot:
        default_values["sort_criterion_radiobutton_value"] = interactive_plot.sort_criterion
        default_values["data_radiobutton_value"] = interactive_plot.dataset_selection
        default_values["show_feature_details_value"] = "True" if interactive_plot.show_feature_details else "False"
        default_values["goodness_of_fit_value"] = "True" if interactive_plot.goodness_of_fit else "False"

    # Handle datasets to be shown in the plot
    if not default_values["data_checklist_value"]:
        default_values["data_checklist_value"] = [default_values["data_radiobutton_value"]]

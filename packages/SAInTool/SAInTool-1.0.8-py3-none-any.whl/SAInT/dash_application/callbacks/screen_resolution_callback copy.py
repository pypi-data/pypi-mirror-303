from dash import Input, Output, State
from dash.exceptions import PreventUpdate
from SAInT.dash_application.pixel_definitions import PixelDefinitions

def register_screen_resolution_callback(dash_app, app):
    # JavaScript code to get screen dimensions
    dash_app.clientside_callback(
        """
        function(n_intervals) {
            return {
                'width': window.innerWidth,
                'height': window.innerHeight
            };
        }
        """,
        Output("screen-dimensions", "children"),
        Input("interval_component", "n_intervals")
    )

    @dash_app.callback(
        Output("app_content", "children"),
        [Input("screen-dimensions", "children")],
        [State("app_content", "children")]  # State to store current layout to avoid re-rendering
    )
    def update_screen_resolution(screen_dims, content):
        # Check if screen dimensions are provided
        if screen_dims:
            width = screen_dims["width"]
            height = screen_dims["height"]
            # If dimensions are not initialized yet, initialize them
            if app.current_screen_dims is None or app.current_screen_dims != screen_dims:
                app.current_screen_dims = screen_dims
                app.application.pixel_definitions = PixelDefinitions(width=width, height=height)
                app._setup_layout()
                app._register_callbacks()
                content = app.app.layout
                print(f"Updated: {width} x {height}")
                return content
        # If dimensions haven't changed, return the current layout (no update)
        #raise PreventUpdate
        return content

import math
from SAInT.dash_application.dash_component import DashComponent, html, dbc

class DashSliderGrid(DashComponent):
    def __init__(self, sliders, id, rows = None, cols = None):
        super().__init__(id=id)
        self.sliders = sliders
        self.rows = rows
        self.cols = cols

    def to_html(self, pixel_def):
        content = []
        sliders = list(self.sliders.values())
        total_sliders = len(sliders)

        # Calculate rows or columns if not provided
        if self.rows is None and self.cols is None:
            raise ValueError("At least one of 'rows' or 'cols' must be specified.")
        if self.rows is None:
            self.rows = math.ceil(total_sliders / self.cols)
        if self.cols is None:
            self.cols = math.ceil(total_sliders / self.rows)

        # Create grid of sliders
        grid = []
        for i in range(0, total_sliders, self.cols):
            row_sliders = sliders[i:i + self.cols]
            # Check if this is the last row and needs filling
            if len(row_sliders) < self.cols:
                # Add empty columns to fill the row
                row_sliders += [dbc.Col() for _ in range(self.cols - len(row_sliders))]
            slider_row = dbc.Row(
                [dbc.Col(slider, width=12 // self.cols) for slider in row_sliders],
                style={"width": "100%"}
            )
            grid.append(slider_row)

        # Return the final layout
        content = html.Div([
            html.Br(),
            html.Div(
                grid,
                id="sliders_container",
                style={
                    "display": "flex",
                    "flex-direction": "column",
                    "justify-content": "space-between",
                    "padding": 5,
                    "align-items": "center"
                })
        ], style = {
                "width": "100%"
            }
        )
        return content

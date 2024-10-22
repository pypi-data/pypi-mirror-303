from SAInT.dash_application.dash_component import DashComponent, html, dbc, dcc

class DashSlider(DashComponent):
    def __init__(self, slider, slider_text, id):
        super().__init__(id=id)
        self.slider = slider
        self.slider_text = slider_text
        self.slider_text_id = {'type': 'slider-text', 'index': self.id["index"]}
        self.classname = "adaptation-slider"
        self.updatemode = "mouseup"
        self.tooltip = {"placement": "bottom",
                        "always_visible": True}

    def to_html(self, pixel_def):
        return html.Div([
                dbc.Label(self.slider["label"]),
                dcc.Slider(id={'type': 'slider', 'index': self.id["index"]},
                           value=self.slider["value"],
                           min=self.slider["min"],
                           max=self.slider["max"],
                           step=self.slider["step"],
                           marks=self.slider["marks"],
                           className=self.classname,
                           tooltip=self.tooltip,
                           updatemode=self.updatemode
                           ),
                html.Br(),
                html.Div(children=self.slider_text,
                         id=self.slider_text_id),
                html.Br(),
                html.Br(),
                html.Br(),
        ])

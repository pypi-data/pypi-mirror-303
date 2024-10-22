from SAInT.dash_application.dash_component import DashComponent, html, dcc
from SAInT.dash_application.components.dash_icon_button import DashIconButton

class DashConsole(DashComponent):
    def __init__(self):
        super().__init__(id="output_preformatted")
        self.name = "Console"
        self.default_value = ""
        self.width = "100%"
        self.clear_button = DashIconButton(
            label="Clear console",
            class_name="fa fa-times",
            id="clear_console_button"
        )

    def to_html(self, pixel_def):
        fontsize = pixel_def.text_font_size
        height = pixel_def.editor_window_height
        return html.Div([
            html.H6(self.name),
            html.Pre(id=self.id,
                     children=self.default_value,
                     style={
                         "width": self.width,
                         "height": height,
                         "font-size": fontsize,
                         "overflow-y": "auto",  # To handle long output
                         "white-space": "pre-wrap"  # To wrap long lines
                     }),
            self.clear_button.to_html(pixel_def)
        ])

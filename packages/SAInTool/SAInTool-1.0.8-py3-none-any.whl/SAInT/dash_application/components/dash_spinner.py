from SAInT.dash_application.dash_component import DashComponent, dbc

class DashSpinner(DashComponent):
    def __init__(self, obj, id):
        super().__init__(id=id)
        self.children = obj
        self.loading_type = "border"

    def to_html(self, pixel_def):
        return dbc.Spinner(children=self.children,
                        id=self.id,
                        type=self.loading_type,
        )

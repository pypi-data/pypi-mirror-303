import dash
from dash import dcc, html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Dash App with Reload Warning"),
    dcc.Input(id='input-box', type='text', placeholder='Type something...'),
    html.Div(id='output')
])

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)

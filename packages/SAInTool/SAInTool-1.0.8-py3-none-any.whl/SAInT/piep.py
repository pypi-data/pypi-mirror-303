import dash
from dash import dcc, html

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Dash App with Reload Warning"),
    
    # Location component to ensure proper page loading
    dcc.Location(id='url', refresh=False),
    
    # Your other app components go here
    
    # Interval component to ensure the script stays active
    dcc.Interval(id='interval', interval=1 * 1000, n_intervals=0),

    # Add the JavaScript as part of the layout
    html.Script('''
        window.addEventListener('beforeunload', function (e) {
            var confirmationMessage = 'You have unsaved data. Do you really want to leave?';
            (e || window.event).returnValue = confirmationMessage; // For modern browsers
            return confirmationMessage; // For older browsers
        });
    ''', type='text/javascript')
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

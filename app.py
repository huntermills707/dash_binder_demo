import dash
from dash import html, dcc, callback, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash on Binder"),
    html.P("This app launched automatically — no clicks required."),
    dcc.Input(id="name-input", type="text", placeholder="Type your name..."),
    html.Div(id="greeting"),
])

@callback(
    Output("greeting", "children"),
    Input("name-input", "value"),
)
def update_greeting(name):
    if not name:
        return ""
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8050)

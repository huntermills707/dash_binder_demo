import os
import dash
from dash import html, dcc, callback, Input, Output

# Build the correct prefix for Binder's proxy path.
# JUPYTERHUB_SERVICE_PREFIX is set automatically by Binder/JupyterHub.
service_prefix = os.environ.get("JUPYTERHUB_SERVICE_PREFIX", "/")
prefix = f"{service_prefix}proxy/8050/"

app = dash.Dash(
    __name__,
    requests_pathname_prefix=prefix,
)

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
    app.run_server(debug=False, host="0.0.0.0", port=8050)

import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    "category": ["A", "B", "C", "D"],
    "value": [4, 1, 3, 5]
})

fig = px.bar(df, x="category", y="value", title="Demo Bar Chart")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Hello from Binder!"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    # Bind to 0.0.0.0 so Binder can reach it
    app.run_server(host="0.0.0.0", port=8050, debug=False)

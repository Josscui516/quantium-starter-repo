import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("data/processed_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Total Sales",
        "region": "Region"
    }
)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Impact of Pink Morsel Price Increase on Sales"),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)


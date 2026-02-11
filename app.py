import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv("data/processed_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[

        html.H1(
            "Impact of Pink Morsel Price Increase on Sales",
            style={
                "textAlign": "center",
                "marginBottom": "30px"
            }
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All Regions", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={
                "textAlign": "center",
                "marginBottom": "30px"
            }
        ),

        dcc.Graph(id="sales-chart")

    ],
    style={
        "fontFamily": "Arial",
        "padding": "40px",
        "backgroundColor": "#f4f4f4"
    }
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        }
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)

import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("output.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

app = dash.Dash(__name__)


app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f4f6f8",
        "padding": "20px"
    },
    children=[
        html.H1(
            "Impact of Pink Morsel Price Increase on Sales",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.Div(
            style={
                "width": "50%",
                "margin": "auto",
                "padding": "10px",
                "backgroundColor": "#ffffff",
                "borderRadius": "8px",
                "boxShadow": "0px 2px 5px rgba(0,0,0,0.1)"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={"fontWeight": "bold"}
                ),

                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginTop": "10px"}
                )
            ]
        ),

        html.Br(),

        html.Div(
            style={
                "backgroundColor": "#ffffff",
                "padding": "15px",
                "borderRadius": "8px",
                "boxShadow": "0px 2px 5px rgba(0,0,0,0.1)"
            },
            children=[
                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
        title = "Pink Morsel Sales – All Regions"
    else:
        filtered_df = df[df["region"] == selected_region]
        title = f"Pink Morsel Sales – {selected_region.capitalize()} Region"

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=title
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Sales"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)

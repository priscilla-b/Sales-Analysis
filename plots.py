import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def trend(df):
    trend_fig = make_subplots(specs=[[{"secondary_y": True}]])
    trend_fig.add_trace(
        go.Bar(
            x=df["Order Date"], y=df["Revenue"],
            name = "Revenue"
        ),
        secondary_y = False
    )
    trend_fig.add_trace(
        go.Bar(
            x=df["Order Date"], y=df["Cost"],
            name = "Cost"
        ),
        secondary_y = False
    )
    trend_fig.add_trace(
        go.Bar(
            x=df["Order Date"], y=df["Profit"],
            name = "Profit"
        ),
        secondary_y = False
    )

    trend_fig.add_trace(
        go.Scatter(
            x=df["Order Date"], y=df["Profit Margin"],
            name = "Profit Margin",
        ),
        secondary_y = True
    )
    trend_fig.update_layout(
        autosize=True,
        margin=dict(
            l=10,
            r=50,
            b=10,
            t=10,
            pad=4
        ),
        legend=dict(
            yanchor="bottom",
            xanchor="left",
            orientation='h',
            y=1.02,
            x=0.1
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"

    )
    return trend_fig

def matrix(df):

    matrix_fig = go.Figure(data = [go.Table(
        columnwidth=[120, 60, 60, 60],
        header = dict(values=list(df.columns),
                    fill_color="gray",
                    line_color="gray",
                    font = dict(color="white", size=12),
                    height=25,
                    align="left"),
        cells =  dict(values=df.T, 
                    fill_color="white",
                    line = dict(color="gray", width=None),
                    font = dict(color="black", size=10),
                    height = 19,
                    align="left")
    )])

    matrix_fig.update_layout(
        autosize=True,
        margin=dict(
            l=10,
            r=50,
            b=10,
            t=10,
            pad=4
        )
    )
    return matrix_fig

def create_map():
    ghana_geo = pd.read_json("data/ghana_regions.json")
    return ghana_geo

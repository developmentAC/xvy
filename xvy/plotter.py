#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import plotly.express as px
import plotly.graph_objects as go

# Create random data with numpy
import numpy as np
from rich.console import Console

console = Console()


def multiplot(
    myTitle_str: str, x0_list: list, y0_list: list, x1_list: list, y1_list: list
) -> None:
    """plots the data along with the regression model line (y1_list from y_pred). Note, the np.array() data structure needs to be converted to a basic Python list before Plotly will work with the list."""
    # these x-axis settings may need attention since unsorted and sorted datasets may upset the x-axis values
    
    # x0 = np.linspace(0, len(y0_list), len(y0_list))  # x_list could be a list of values
    x0 = np.linspace(0, 1, len(y0_list))  # x_list could be a list of values
    # x1 = np.linspace(0, len(x1_list), len(x1_list))  # x_list could be a list of values
    x1 = np.linspace(0, 1, len(y1_list))  # x_list could be a list of values

    # Need to convert np.array() to a simple python list.
    # Not sure why Plotly is unable to handle np.array() structures... ?
    # The conversion has been an emotional journey.
    # the below conversion is now done in each model function in main().
    # y_list = y1_list.tolist()
    # y1_list = [i[0] for i in y_list]

    # Create traces
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x0,
            y=y0_list,
            mode="markers",  # could use: "lines+markers"
            name="Original Data",
            xaxis="x",
        )
    )
    fig.add_trace(
        go.Scatter(x=x1, y=y1_list, mode="lines+markers", name="Predicted")
    )  # working

    myTitle_str = str(myTitle_str)
    # console.print(f"data file is: {myTitle_str}, {type(myTitle_str)}")

    myTitle_str = myTitle_str[myTitle_str.find("/") + 1 :]
    # fig.update_layout(height=800, title_text='MY title')
    fig.update_layout(title_text=myTitle_str)

    fig.show()


# end of multiplot()

##################################
# play with outher plots. See code below.


def randomPlot(x1_list: list, y1_list: list, x2_list, y2_list) -> None:
    import plotly.graph_objects as go

    # Create random data with numpy
    import numpy as np

    np.random.seed(1)

    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5

    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=random_x, y=random_y0, mode="lines", name="lines"))
    fig.add_trace(
        go.Scatter(x=random_x, y=random_y1, mode="lines+markers", name="lines+markers")
    )
    fig.add_trace(go.Scatter(x=random_x, y=random_y2, mode="markers", name="markers"))

    fig.show()


# end of randomPlot()


def plotPlotly(x_list: list, y_list: list) -> None:
    """plots one line"""
    # x and y given as array_like objects
    # fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    if len(x_list) != len(y_list):
        console.print(" Error in sizes of data sets...")
        exit()

    fig = px.scatter(x_list, y_list)
    fig.show()


# end of plotPlotly()


def old_multiplot(x1_list: list, y1_list: list, x2_list, y2_list) -> None:
    """plots two lines"""
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    trace1 = go.Bar(
        x=df[cat], y=df[num], name=num, marker=dict(color="rgb(34,163,192)")
    )
    trace2 = go.Scatter(
        x=df[cat], y=df["cumulative_perc"], name="Cumulative Percentage", yaxis="y2"
    )

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(trace1)
    fig.add_trace(trace2, secondary_y=True)
    fig["layout"].update(height=600, width=800, title=title, xaxis=dict(tickangle=-90))
    iplot(fig)
    # end of old_multiplot()

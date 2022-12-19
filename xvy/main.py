#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# see more example code at
# https://hub.gke2.mybinder.org/user/scikit-learn-scikit-learn-m20vqp5l/lab/tree/notebooks/auto_examples/linear_model/plot_ols.ipynb

from xvy import plotter as pl
from xvy import launcher

from rich.console import Console

import typer

from pathlib import Path

import numpy as np

from sklearn.linear_model import LinearRegression

console = Console()

# create a Typer object to support the command-line interface
cli = typer.Typer()


@cli.command()
def main(
    data_file: Path = typer.Option(None),
    bighelp: bool = False,
    showData: bool = False,

) -> None:
    """Summarize the data values stored in a file."""
    # display details about the file provided on the command line
    data_text = ""
    # --> the file was not specified so we cannot continue using program
    if bighelp: 
        launcher.helper()
        exit()

    if data_file is None:
        console.print("No data file specified!")
        raise typer.Abort()
    # --> the file was specified and it is valid so we should read and check it
    if data_file.is_file() == False:
        console.print(f"Oh :poop:! Error with file. Exiting...")
        exit()  # :thumbs_down:

    myData_str = openFile(data_file)  # Open file, get string
    xoriginal_list, x_list, y_list = wrangleData(
        myData_str, showData
    )  ## wrangle data: get data in numpy form

    # y_predModel = runModel(x_list, y_list)
    # pl.multiplot(x_list, y_list, y_predModel)
    # print(f"yPred : {y_predModel}, {type(y_predModel)}")

    y_predNewModel = runNewModel(x_list, y_list)

    pl.multiplot(data_file, x_list, y_list, xoriginal_list, y_predNewModel)

    if showData:
        console.print(f"yPred : {y_predNewModel}, {type(y_predNewModel)}")

    # pl.plotPlotly(x_list, y_list) # debugging


# end of main()


def openFile(data_file: str) -> str:
    """function to open and read the cvs file. Returns data as str"""
    data_text = data_file.read_text()
    return data_text


# end of openFile


def wrangleData(data_text: str, showData) -> str:
    """convert string to numpy data form"""

    data_line_count = len(data_text.splitlines())
    console.print(
        f":microscope: The data file contains {data_line_count} data values in it!! :cake:"
    )

    # console.print(f"data_text : {data_text} ")
    listedItems = data_text.splitlines()
    x_list = []
    y_list = []
    for line in listedItems:
        lline = line.split(",")
        # print(lline)

        try:
            x_list.append(float(lline[0]))
        except ValueError:
            console.print(f"Error with {lline[0]}")
        try:
            y_list.append(float(lline[1]))
        except ValueError:
            console.print(f"Error with {lline[1]}")

    if showData:
        if len(x_list) == len(y_list):
            console.print("\n\t Data:\n\t n : x , y\n\t ---------")
            for i in range(len(x_list)):
                console.print(f"\t {i} : {x_list[i]:.1f}, {y_list[i]:.1f} ", style="White")
            console.print("\n")

    # console.print(f"\t [+] x_list : {x_list}: {type(x_list)}")
    # console.print(f"\t [+] y_list : {y_list}: {type(y_list)}")

    x = np.array(x_list).reshape((-1, 1))
    y = np.array(y_list)
    return x_list, x, y  # x_list is original, x and y are np.array()


# end of wrangleData()

# def makeModelLine():
# # end of makeModelLine()


def runModel(xData, yData) -> list:
    """define and run the model"""
    model = LinearRegression()
    # model.fit(xData, yData)
    model = LinearRegression().fit(xData, yData)
    r_sq = model.score(xData, yData)
    console.print(f"\t", "=" * 30)
    console.print(f"\t [+] Multiple R-squared: {r_sq}")
    console.print(f"\t [+] Intercept: {model.intercept_}")
    console.print(f"\t [+] Slope: {model.coef_}")
    console.print(
        f"\t [+] Model Line formula : y = {model.coef_} * x + {model.intercept_}"
    )

    console.print(f"\n")
    y_pred = model.predict(xData)
    # console.print(f"\t [+] Predicted response:\n{y_pred}")

    y_list = y_pred.tolist()
    y1_list = [i for i in y_list]

    return y1_list


# end of runModel()


def runNewModel(xData, yData):
    """define and run another model with new fitting"""
    model = LinearRegression().fit(xData, yData.reshape((-1, 1)))
    r_sq = model.score(xData, yData)
    console.print(f"\t [+] NM: Multiple R-squared: {r_sq}")  # , style="blue on cyan")
    console.print(f"\t [+] NewMod: intercept: {model.intercept_}")
    console.print(f"\t [+] NewMod: slope: {model.coef_}")
    console.print(
        f"\t [+] Model Line formula : y = {model.coef_[0][0]} * x + {model.intercept_[0]}"
    )

    console.print(f"\n")
    y_pred = model.predict(xData)
    # console.print(f"\t [+] NewMod: predicted response:\n{y_pred}")

    y_list = y_pred.tolist()
    y1_list = [i[0] for i in y_list]

    return y1_list


# end of runNewModel()

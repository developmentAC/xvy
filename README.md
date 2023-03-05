# XvY: A Simple Linear Regression Calculator

## Date

19 Dec 2022

![graphics/xvsy.png](graphics/xvsy.png)

## Detail

This is a regression calculator of data column $x$ over data column $y$ from the input file. The output is an interactive graph that opens in the default browser.

## Data

The `csv` files will take the following form. The `x` column (first) is separated from the `y` column (second).

```
1,15
2,14
3,18
4,17
5,20
6,17
7,18
8,16
9,20
10,29
11,29
12,34
13,40
14,49
15,52
16,41
17,50
18,45
19,52
20,51
21,57
22,51
```

## Dependencies

The necessary libraries for this project are listed below. To make the installation of these dependencies easier on the user, we use `Poetry` to manage the project.

```
tool.poetry.dependencies]
python = "^3.8"
numpy = "^1.23.5"
rich = "^12.6.0"
typer = "^0.7.0"
black = "^22.12.0"
sklearn = "^0.0.post1"
scikit-learn = "^1.2.0"
plotly = "^5.11.0"
pandas = "^1.5.2"
matplotlib = "^3.6.2"
```

## Running the program

You must first install [Poetry](https://python-poetry.org/) to manage the code's dependencies, and to run the program.

To run the program, enter the following commands.

* In the root directory of the project. Note this is where you will find the file, `pyproject.toml`
  + `poetry install`
* Run the program.
  + `poetry run xvy --data-file input/majors.csv`
* Get help in using the program (i.e., find out what the parameters are).
  + `poetry run xvy --help`
* See the splash page.
  + `poetry run xvy --bighelp`

## Output

In the terminal window, the y-predicted values will be shown. These values give the red line in the Plotly plot which is outputted.

![graphics/plot.png](graphics/plot.png)


## A work in progress

Check back often to see the evolution of the project!! Updates to the methods and tests for the code will come soon and I will continue to update the repository with updates. If you would like to contribute to this project, __then please do!__ For instance, if you see some low-hanging fruit or task that you could easily complete, that could add value to the project, then I would love to have your insight.

Otherwise, please create an Issue for bugs or errors. Since I am a teaching faculty member at Allegheny College, I may not have all the time necessary to quickly fix the bugs and so I would be very happy to have any help that I can get from the OpenSource community for any technological insight. Much thanks in advance. I hope that this project is helpful to you in some way. :-)

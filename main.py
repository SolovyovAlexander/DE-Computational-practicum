import matplotlib.pyplot as plt
import math


def main(h):
    X = 3
    y0 = 0
    x0 = 0
    n = (X - x0) / h
    x_points = []  # list of x points
    # filling the list depending on the step size
    for i in range(int(n) + 1):
        if i == 0:
            x_points.append(x0)
        else:
            x = x_points[i - 1] + h
            x_points.append(x)
    # methods call with arguments
    eulers_method(x_points, h, X, y0)
    improved_Eulers_method(x_points, h, X, y0)
    Runge_Kutta(x_points, h, X, y0)
    # exact solution
    exact_solution(x_points)

    # title of graph
    plt.title("Graph of function  y = 2*x - 1 + e^(-2*x)  ")

    # labels of x and y axises
    plt.xlabel("X")
    plt.ylabel("Y")

    # legend for plots
    plt.legend(["euler", "improved euler", "Runge Kutta", "exact solution"])

    # setting the size of the graph
    fig = plt.gcf()
    fig.set_size_inches(19.5, 10.6, forward=True)

    # adding a grid
    plt.grid()

    # save plot as file
    plt.savefig("h=0.1.pdf")

# implementation of exact solution
def exact_solution(x_points):
    y_points = []
    for i in range(len(x_points)):
        y_points.append(2 * x_points[i] - 1 + math.exp(-2 * x_points[i]))

    plt.plot(x_points, y_points, "b.-")

# function f(x;y) from y'=f(x;y)
def function(x, y):
    return -2 * y + 4 * x


# implementation of euler's method Yi+1=Yi+h*f(Xi;Yi)
def eulers_method(x_points, h, X, y0):
    n = (X - x_points[0]) / h  # number of steps
    y_points = []  # list of y points
    for i in range(int(n) + 1):
        if i == 0:
            y_points.append(y0)
        else:
            y = y_points[i - 1] + h * function(x_points[i - 1], y_points[i - 1])
            y_points.append(y)
    plt.plot(x_points, y_points, "r.-")  # build a plot of red colour

# implementation of improved euler's method
def improved_Eulers_method(x_points, h, X, y0):
    n = (X - x_points[0]) / h  # number of steps
    y_points = []  # list of y points
    for i in range(int(n) + 1):
        if i == 0:
            y_points.append(y0)
        else:
            y_delta = h * function(x_points[i - 1] + h / 2,
                                   y_points[i - 1] + function(x_points[i - 1], y_points[i - 1]) * h / 2)
            y = y_points[i - 1] + y_delta
            y_points.append(y)
    plt.plot(x_points, y_points, "g.-")  # build a plot of green colour

# implementation of Runge-Kutta method
def Runge_Kutta(x_points, h, X, y0):
    n = (X - x_points[0]) / h  # number of steps
    y_points = []  # list of y points
    for i in range(int(n) + 1):
        if i == 0:
            y_points.append(y0)
        else:
            k1 = function(x_points[i - 1], y_points[i - 1])
            k2 = function(x_points[i - 1] + h / 2, y_points[i - 1] + (h * k1 / 2))
            k3 = function(x_points[i - 1] + h / 2, y_points[i - 1] + (h * k2 / 2))
            k4 = function(x_points[i - 1] + h, y_points[i - 1] + h * k3)
            y_delta = (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
            y = y_points[i - 1] + y_delta
            y_points.append(y)
    plt.plot(x_points, y_points, "y.-")  # build a plot of yellow colour


main(0.1)  # call all methods with a step of 0.1

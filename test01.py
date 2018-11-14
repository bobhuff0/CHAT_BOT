#
#
# SIMPLE
#
# Plots square root function from 0 to 100

import base64
import json
import matplotlib, matplotlib.pyplot
import numpy
import types

def show_plot(width, height=None):
    """
    A decorator -- show the matplotlib plot after `f` completes.
    Takes optional parameters (width, height) determining the size of the plot.
    """
    def const_decorator(f):
        def wrapped_f(*args, **kwargs):
            fig=matplotlib.pyplot.figure(figsize=(width, height))
            ret = f(*args, **kwargs)
            matplotlib.pyplot.show()
            return ret
        return wrapped_f
    if type(width)==types.FunctionType:
        f = width
        width, height = 9, 4
        return const_decorator(f)
    else:
        return const_decorator


def output_image(*args, **kwargs):
    raise NotImplementedError

import re
import requests
import math
##from udacityplots import *

@show_plot
def simple():
    x_data = numpy.linspace(0., 100., 1000)

    for x in x_data:
        y = math.sqrt(x)
        matplotlib.pyplot.scatter(x, y)

    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('x')
    axes.set_ylabel('y')
    axes.set_xlabel('boo')

simple()
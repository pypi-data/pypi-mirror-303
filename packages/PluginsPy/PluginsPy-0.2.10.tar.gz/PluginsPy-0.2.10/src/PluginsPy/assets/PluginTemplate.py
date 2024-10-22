#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: ${author}
Date: ${date}
License: MIT License
"""

import datetime

from PluginsPy.VisualLogPlot import VisualLogPlot

import VisualLog.LogParser as LogParser
import VisualLog.MatplotlibZoom as MatplotlibZoom

import matplotlib.pyplot as plot
from matplotlib.figure import Figure
from matplotlib.axes import Axes

class ${className}:

    """
    ${defaultArgs}
    """

    def __init__(self, kwargs):

        print("${className} args:")
        print(kwargs)

        ${instanceArgs}

        parseFilenames = [${parseFilenames}]
        regex = [${regex}]
        kwargs["lineInfosFiles"], filenames = LogParser.logFileParser(
            parseFilenames,
            regex,
            )

        plotType             = "${plotType}"
        kwargs["xAxis"]      = [${xAxis}]
        kwargs["dataIndex"]  = [${dataIndex}]

        if plotType == "normal":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "key":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "keyLoop":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyLoopShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "keyDiff":
            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyDiffShowCallback, rows = 1, cols = 1, args=kwargs)
        elif plotType == "3D":
            MatplotlibZoom.Show(callback=VisualLogPlot.default3DShowCallback, rows = 1, cols = 1, d3=True, args=kwargs)
        else:
            print("unsupport plot type")

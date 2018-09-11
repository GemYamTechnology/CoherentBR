#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
"""
20180711加上製作圖片的模組，讓製圖時比較方便，可惜沒有成功
"""
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

def InputLines1(Lines):
    ax1.clear()
    X = []
    Y = []
    for line in Lines:
        if len(line) > 1:
            x, y = line.split(',')
            X.append(int(x))
            Y.append(int(y))
    AllList = X, Y
    return AllList

def InputLines2(Lines):
    X = []
    Y = []
    y = 0
    for lines in Lines:
        for line in lines:
            y += 1
            if len('int(line)') > 1:
                Y.append(int(line))
                X.append(int(y))
    AllList = X, Y
    return AllList

def AnimateShow(X, Y):
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.clear()
    ax1.plot(X, Y, linewidth=1)
    #ani = animation.FuncAnimation(fig, animate, interval=1)
    plt.show()

def animate(X, Y):
    ax1.clear()
    ax1.plot(X, Y, linewidth=1)

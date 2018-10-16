#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
#Derive from "tcp_echo_server_0101bOK"

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

class DI:
    def __init__(DIself, Lines = [1850826, 1846028, 1858695, 1846032, 1851374, 1844861, 1854828, 1855687, 1850826, 1846028, 1858695, 1846032, 1851374, 1844861, 1854828, 1855687], Path = "./Data.csv"):
        DIself.Lines = Lines
        DIself.Path = Path
        DIself.X = 0
        fig = plt.figure()
        DIself.Fig = fig
        DIself.Ax = fig.add_subplot(1,1,1)

    def Animate(DIself):
        xs1 = []
        ys1 = []
        for line in DIself.Lines:
            DIself.X += 1
            y = line
            xs1.append(int(DIself.X))
            ys1.append(int(y))
        DIself.Ax.clear()
        return DIself.Ax.plot(xs1,ys1,linewidth=1)

    def Show_1(DIself):
        ani = animation.FuncAnimation(DIself.Fig, DI.Animate(),interval=1)
        plt.show()

DI = DI()
DI.Show_1()

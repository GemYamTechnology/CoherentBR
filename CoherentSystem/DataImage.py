#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
#Derive from "tcp_echo_server_0101bOK"
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

class DataImage:
    def __init__(self):
        fig = plt.figure()
        self.Fig = fig
        ax1 = fig.add_subplot(1,1,1)
        x = 0
        xs1 = []
        ys1 = []
        for line in lines:
            x += 1
            y = line
            xs1.append(int(x))
            ys1.append(int(y))

        ax1.clear()
        self.Ax1 = ax1.plot(xs1,ys1,linewidth=1)

    def animate(self, lines):
        style.use('fivethirtyeight')
        ani = animation.FuncAnimation(self.Fig, self.Ax1,interval=1)
        plt.show()

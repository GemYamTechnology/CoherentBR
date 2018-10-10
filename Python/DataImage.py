#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
#Derive from "tcp_echo_server_0101bOK"

"""
A simple "tcp echo server" for demonstrating TCP usage.
The server listens for TCP packets and echoes any received
packets back to the originating host.

"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

class DI:
    def __init__(self, Lines = [1850826, 1846028, 1858695, 1846032, 1851374, 1844861, 1854828, 1855687], Path = "./Data.csv"):
        self.Lines = Lines
        self.Path = Path
        self.X = 0
        self.Fig = plt.figure()
        self.Ax = self.Fig.add_subplot(1,1,1)

    def Animate(self):
        xs1 = []
        ys1 = []
        for line in self.Lines:
            self.X += 1
            y = line
            xs1.append(int(self.X))
            ys1.append(int(y))
        self.xs1 = xs1
        self.ys1 = ys1
        self.Ax.clear()
        self.Ax.plot(xs1,ys1,linewidth=1)

    def Show(self):
        ani = animation.FuncAnimation(self.Fig, self.Animate(),interval=1)
        plt.show()

DI = DI()
DI.Show()

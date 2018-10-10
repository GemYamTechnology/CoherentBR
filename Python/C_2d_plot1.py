#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
#Derive from "tcp_echo_server_0101bOK"

"""
A simple "tcp echo server" for demonstrating TCP usage.
The server listens for TCP packets and echoes any received
packets back to the originating host.

"""
import DecodeString
import sys
import string
import TCP
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
FileName = "H:/Data.csv"
def animate(i):
    ServerHost, ServerPort = "",50007
    x = 0
    conn, addr, ServerHost, ServerPort = TCP.EchoClient(ServerHost, ServerPort)
    date, ClientIP, ClientPort, ServerHost, ServerPort, ReprData = TCP.EchoData(conn, addr, ServerHost, ServerPort)
    LinesList = DecodeString.RCTCLDCOBSDC(ReprData)
    for Lines in LinesList:
        xs1 = []
        ys1 = []
        for Line in Lines:
            x += 1
            y = Line
            xs1.append(int(x))
            ys1.append(int(y))
    ax1.clear()
    ax1.plot(xs1,ys1,linewidth=1)

ani = animation.FuncAnimation(fig, animate,interval=1)
plt.show()

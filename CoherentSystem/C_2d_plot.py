#!/usr/bin/python
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

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data1 = open('249recv_text1.csv','r').read()
    graph_data2 = open('252recv_text1.csv','r').read()
    lines1 = graph_data1.split('\n')
    lines2 = graph_data2.split('\n')
    xs1 = []
    ys1 = []
    xs2 = []
    ys2 = []    
    for line in lines1:
        if len(line) > 1:
            x, y = line.split(',')
            xs1.append(int(x))
            ys1.append(int(y))
            
    for line in lines2:
        if len(line) > 1:
            x, y = line.split(',')
            xs2.append(int(x))
            ys2.append(int(y))
                        
    ax1.clear()
    ax1.plot(xs1,ys1,linewidth=1)
    ax1.plot(xs2,ys2,linewidth=1)
    
ani = animation.FuncAnimation(fig, animate,interval=1)
plt.show()

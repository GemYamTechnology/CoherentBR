# Derive from "recv_Laisan3.py"

import pandas
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.gca(projection='3d')

# Set background color of matplotlib
#ax.set_facecolor('xkcd:salmon')
ax.set_facecolor((0, 0.3, 0.7))

N=3000
xs = np.arange(0, N, 1)
zs = [0, 1, 2, 3, 4, 5, 6, 7]
verts = []

def cc(arg):
    return mcolors.to_rgba(arg)

def plot_cont():
    def update(i):
        global xs
        global zs
        global verts

        data1 = "recv_text1.csv"
        names1 = ['x_signal','y_signal']
        dataset1 = pandas.read_csv(data1, names=names1)
        data2 = "recv_text2.csv"
        names2 = ['x_signal','y_signal']
        dataset2 = pandas.read_csv(data2, names=names2)
        data3 = "recv_text3.csv"
        names3 = ['x_signal','y_signal']
        dataset3 = pandas.read_csv(data3, names=names3)
        data4 = "recv_text4.csv"
        names4 = ['x_signal','y_signal']
        dataset4 = pandas.read_csv(data4, names=names4)
        data5 = "recv_text5.csv"
        names5 = ['x_signal','y_signal']
        dataset5 = pandas.read_csv(data5, names=names5)
        data6 = "recv_text6.csv"
        names6 = ['x_signal','y_signal']
        dataset6 = pandas.read_csv(data6, names=names6)
        data7 = "recv_text7.csv"
        names7 = ['x_signal','y_signal']
        dataset7 = pandas.read_csv(data7, names=names7)
        data8 = "recv_text8.csv"
        names8 = ['x_signal','y_signal']
        dataset8 = pandas.read_csv(data8, names=names8)

        array1 = dataset1.values
        y1= array1[:,1]
        array2 = dataset2.values
        y2= array2[:,1]
        array3 = dataset3.values
        y3= array3[:,1]
        array4 = dataset4.values
        y4= array4[:,1]
        array5 = dataset5.values
        y5= array5[:,1]
        array6 = dataset6.values
        y6= array6[:,1]
        array7 = dataset7.values
        y7= array7[:,1]
        array8 = dataset8.values
        y8= array8[:,1]
		
        verts = []
        verts.append(list(zip(xs, y1)))
        verts.append(list(zip(xs, y2)))
        verts.append(list(zip(xs, y3)))
        verts.append(list(zip(xs, y4)))
        verts.append(list(zip(xs, y5)))
        verts.append(list(zip(xs, y6)))
        verts.append(list(zip(xs, y7)))
        verts.append(list(zip(xs, y8)))

        ax.clear()
        poly = PolyCollection(verts, facecolors=[cc('r'), cc('g'), cc('b'),
                                                 cc('y'), '#830015', '#7F377F',
    										     cc('m'), cc('w')])
        poly.set_alpha(0.7)
        ax.add_collection3d(poly, zs=zs, zdir='y')

        ax.set_xlabel('Time [ms]')
        ax.set_xlim3d(0, len(y1))
        ax.set_ylabel('Channel')
        ax.set_ylim3d(-1, len(zs)+1)
        ax.set_zlabel('Amp.')
        ax.set_zlim3d(-8388606, 8388607)

    a = animation.FuncAnimation(fig, update, interval=100, repeat=True)
    plt.show()

plot_cont()

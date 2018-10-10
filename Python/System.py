#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# Derive from: recv_Laisan2
import DecodeString
from DataImage import *
import sys
import string
import TCP
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

FileName = "H:/Data.csv"
ServerHost, ServerPort = "",50007

while (1):
    conn, addr, ServerHost, ServerPort = TCP.EchoClient(ServerHost, ServerPort)
    date, ClientIP, ClientPort, ServerHost, ServerPort, ReprData = TCP.EchoData(conn, addr, ServerHost, ServerPort)
    LinesList = DecodeString.RCTCLDCOBSDC(ReprData)
    for Lines in LinesLiset:
        for Line in Lines:
            Data = date + "," + LinesList
            FA.AddDataCSV(FileName, Data)

#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# Derive from: recv_Laisan2
import DecodeString
import sys
import string
import TCP
import FileAccess as FA

FileName = "../Data/Data.csv"
ServerHost, ServerPort = "",50007

while (1):
    LinesList = ""
    conn, addr, ServerHost, ServerPort = TCP.EchoClient(ServerHost, ServerPort)
    date, ClientIP, ClientPort, ServerHost, ServerPort, ReprData = TCP.EchoData(conn, addr, ServerHost, ServerPort)
    LinesList = DecodeString.RCTCLDCOBSDC(ReprData)
    for Lines in LinesList:
        for Line in Lines:
            Data = str(date) + "," + str(Line) + "\n"
            FA.AddDataCSV(FileName, Data)

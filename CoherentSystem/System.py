#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# Derive from: recv_Laisan2
import DecodeString
import DataImage as DI
import sys
import string
import TCP

ServerHost, ServerPort = "",50007
DI = DI()
while (1):
    conn, addr, ServerHost, ServerPort = TCP.EchoClient(ServerHost, ServerPort)
    date1, ClientIP, ClientPort, ServerHost, ServerPort, ReprData = TCP.EchoData(conn, addr, ServerHost, ServerPort)
    lines = DecodeString.RCTCLDCOBSDC(ReprData)
    for line in lines:
        print line
        DI.animate(line)

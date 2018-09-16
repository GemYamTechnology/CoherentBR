#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# Derive from: recv_Laisan2
import DecodeString
import DataImage
import sys
import string
import TCP

#X, Y = DataImage.InputLines2(DecodedSequenceList)
#DataImage.AnimateShow(X, Y)

ServerHost, ServerPort = "",50007
while(1):
    conn, addr, ServerHost, ServerPort = TCP.EchoClient(ServerHost, ServerPort)
    date1, ClientIP, ClientPort, ServerHost, ServerPort, ReprData = TCP.EchoData(conn, addr, ServerHost, ServerPort)

while(1):
    DecodedSequenceList = DecodeString.RCTCLDCOBSDC(ReprData)

#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
"""
A simple "tcp echo server" for demonstrating TCP usage.
The server listens for TCP packets and echoes any received
packets back to the originating host.
20180907使用TCP模組來進行程式的簡化，會將內容轉移到System.py
"""
import TCP

ServerHost, ServerPort = "",50007
while(1):
    conn, addr, ServerHost, ServerPort = TCP.EchoClient(ServerHost, ServerPort)
    date1, ClientIP, ClientPort, ServerHost, ServerPort, ReprData = TCP.EchoData(conn, addr, ServerHost, ServerPort)

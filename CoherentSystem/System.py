#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# Derive from: recv_Laisan2
import DecodeString
import DataImage
import sys
import string
import TCP

String = "b9,18,7d,76,18,ac,34,18,89,6d,18,8c,4e,18,74,67,18,b5,e0,18,7d,3a,01,01,01,00,03,ff,a3,1c,01,cd,bf,18,7b,c2,18,7d,39,18,ac,2d,18,89,63,18,8c,33,18,74,56,18,b5,e6,18,7d,44,01,01,01,00,03,f0,a3,1c,01,cd,c0,18,7b,c5,18,7d,3a,18,ac,2d,18,89,66,18,8c,35,18,74,58,18,b5,e8,18,7d,46,01,01,01,00,03,f1,a3,1c,01,cd,c1,18,7b,c4,18,7d,37,18,ac,2d,18,89,67,18,8c,36,18,74,58,18,b5,e7,18,7d,46,01,01,01,00,03,f2,a3,1c,01,cd,c2,19,2d,f4,18,ed,ed,19,39,91,19,19,3b,19,13,10,18,fb,79,19,5e,d9,19,40,0e,01,01,01,00,03,f3,a3,1c,01,cd,c3,1b,de,01,1b,9f,b3,1b,ee,b6,1b,c2,d5,1b,ca,d4,1b,b1,cd,1b,fb,c1,1b,de,5c,01,01,01,00,03,f4,a3,1c,01,cd,c4,1c,30,b6,1c,2b,0c,1c,5c,8a,1c,2b,15,1c,3f,f5,1c,26,83,1c,4d,67,1c,22,ca,01,01,01,00,03,f5,a3,1c,01,cd,c5,1c,30,b3,1c,2b,09,1c,5c,86,1c,2b,12,1c,3f,f1,1c,26,7e,1c,4d,65,1c,22,c7,01,01,01,00,03,f6,a3,1c,01,cd,c6,1c,30,af,1c,2b,08,1c,5c,84,1c,2b,0f,1c,3f,ee,1c,26,7a,1c,4d,64,1c,22,c4,01,01,01,00,03,f7,a3,1c,01,cd,c7,1c,30,b3,1c,2b,0e,1c,5c,89,1c,2b,13,1c,3f,f3,1c,26,80,1c,4d,6a,1c,22,ca,01,01,01,00,03,f8,a3,1c,01,cd,c8,1c,30,4e,1c,2b,0d,1c,5c,88,1c,2b,12,1c,3f,f1,1c,26,80,1c,4d,6b,1c,26,46,01,01,01,00,03,f9,a3,1c,01,cd,c9,1c,3d,ca,1c,2b,0c,1c,5c,87,1c,2b,10,1c,3f,ee,1c,26,7d,1c,4d,6c,1c,50,c7,01,01,01,00,03,fa,a3,1c,01,cd,ca,1c,44,28,1c,2b,0a,1c,5c,84,1c,2b,0e,1c,3f,"

a = DecodeString.RCTCLDCOBSDC(String)
b = DataImage.InputLines2(a)
DataImage.AnimateShow(b)

ServerHost, ServerPort = "",50007
while(1):
	conn, addr, ServerHost, ServerPort = TCP.EchoClient(ServerHost, ServerPort)
	date1, ClientIP, ClientPort, ServerHost, ServerPort, ReprData = TCP.EchoData(conn, addr, ServerHost, ServerPort)

while(1):
	DecodeString.RCTCLDCOBSDC(ReprData)

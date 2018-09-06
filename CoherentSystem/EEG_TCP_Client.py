#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import socket
import time

Counter = 0
String = "b9,18,7d,76,18,ac,34,18,89,6d,18,8c,4e,18,74,67,18,b5,e0,18,7d,3a,01,01,01,00,03,ff,a3,1c,01,cd,bf,18,7b,c2,18,7d,39,18,ac,2d,18,89,63,18,8c,33,18,74,56,18,b5,e6,18,7d,44,01,01,01,00,03,f0,a3,1c,01,cd,c0,18,7b,c5,18,7d,3a,18,ac,2d,18,89,66,18,8c,35,18,74,58,18,b5,e8,18,7d,46,01,01,01,00,03,f1,a3,1c,01,cd,c1,18,7b,c4,18,7d,37,18,ac,2d,18,89,67,18,8c,36,18,74,58,18,b5,e7,18,7d,46,01,01,01,00,03,f2,a3,1c,01,cd,c2,19,2d,f4,18,ed,ed,19,39,91,19,19,3b,19,13,10,18,fb,79,19,5e,d9,19,40,0e,01,01,01,00,03,f3,a3,1c,01,cd,c3,1b,de,01,1b,9f,b3,1b,ee,b6,1b,c2,d5,1b,ca,d4,1b,b1,cd,1b,fb,c1,1b,de,5c,01,01,01,00,03,f4,a3,1c,01,cd,c4,1c,30,b6,1c,2b,0c,1c,5c,8a,1c,2b,15,1c,3f,f5,1c,26,83,1c,4d,67,1c,22,ca,01,01,01,00,03,f5,a3,1c,01,cd,c5,1c,30,b3,1c,2b,09,1c,5c,86,1c,2b,12,1c,3f,f1,1c,26,7e,1c,4d,65,1c,22,c7,01,01,01,00,03,f6,a3,1c,01,cd,c6,1c,30,af,1c,2b,08,1c,5c,84,1c,2b,0f,1c,3f,ee,1c,26,7a,1c,4d,64,1c,22,c4,01,01,01,00,03,f7,a3,1c,01,cd,c7,1c,30,b3,1c,2b,0e,1c,5c,89,1c,2b,13,1c,3f,f3,1c,26,80,1c,4d,6a,1c,22,ca,01,01,01,00,03,f8,a3,1c,01,cd,c8,1c,30,4e,1c,2b,0d,1c,5c,88,1c,2b,12,1c,3f,f1,1c,26,80,1c,4d,6b,1c,26,46,01,01,01,00,03,f9,a3,1c,01,cd,c9,1c,3d,ca,1c,2b,0c,1c,5c,87,1c,2b,10,1c,3f,ee,1c,26,7d,1c,4d,6c,1c,50,c7,01,01,01,00,03,fa,a3,1c,01,cd,ca,1c,44,28,1c,2b,0a,1c,5c,84,1c,2b,0e,1c,3f,"
String2 =  "a1,d7,1c,a2,07,1c,b5,17,1c,d4,9c,01,01,01,00,03,f6,a3,1c,01,cd,a6,1c,a2,b0,1c,7a,ce,1c,b5,67,1c,a3,fc,1c,a1,d5,1c,a1,fe,1c,b5,15,1c,d4,9b,01,01,01,00,03,f7,a3,1c,01,cd,a7,1c,a2,b4,1c,7a,d2,1c,b5,6b,1c,a3,ff,1c,a1,da,1c,a2,02,1c,b5,19,1c,d4,a0,01,01,01,00,03,f8,a3,1c,01,cd,a8,1c,a2,b4,1c,7a,d2,1c,b5,6d,1c,a3,ff,1c,a1,da,1c,a2,02,1c,b5,19,1c,d4,9f,01,01,01,00,03,f9,a3,1c,01,cd,a9,1c,a2,b0,1c,7a,ce,1c,b5,6c,1c,a3,fb,1c,a1,d7,1c,a1,fe,1c,b5,16,1c,d4,9c,01,01,01,00,03,fa,a3,1c,01,cd,aa,1c,a2,a7,1c,7a,c5,1c,b5,64,1c,a3,f2,1c,a1,cf,1c,a1,f7,1c,b5,0d,1c,d4,94,01,01,01,00,03,fb,a3,1c,01,cd,ab,1c,9b,1a,1c,78,44,1c,b2,07,1c,9f,c7,1c,9e,e1,1c,9e,76,1c,ae,a7,1c,cb,df,01,01,01,00,03,fc,a3,1c,01,cd,ac,1a,9b,77,1a,ca,01,1a,e8,1f,1a,ca,b4,1a,ea,cd,1a,d8,2a,1a,b5,a1,1a,b7,c7,01,01,01,00,03,fd,a3,1c,01,cd,ad,18,b6,d3,18,92,e4,18,c8,b4,18,ad,ee,18,d3,7e,18,bb,59,18,c8,30,18,e0,5b,01,01,01,00,03,fe,a3,1c,01,cd,ae,18,b0,10,18,81,8d,18,bc,bc,18,a1,bb,18,c6,16,18,ae,63,18,c1,7d,18,db,4e,01,01,01,00,03,ff,a3,1c,01,cd,af,18,b0,19,18,81,96,18,bc,c6,18,a1,c4,18,c6,1e,18,ae,6d,18,c1,87,18,db,58,01,01,01,00,03,f0,a3,1c,01,cd,b0,18,b0,1c,18,81,9a,18,bc,ca,18,a1,c7,18,c6,1f,18,ae,70,18,c1,89,18,db,5a,01,01,01,00,03,f1,a3,1a,01,cd,b1,18,ce,52,18,8d,66,18,cf,c5,18,b6,f0,18,d7,18,18,bf,b3,18,df,af,19,02,f7,q1,"
List = [String, String2]
while(1):
	print "Counter", Counter

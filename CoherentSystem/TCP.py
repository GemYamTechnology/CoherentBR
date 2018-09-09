#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import socket
import optparse
import time
import datetime
import sys
import DataBase

def EEG_TCP_Client(target_host, target_port, string):
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	client.connect((target_host, target_port))

	client.send(string)

	response = client.recv(4096)
	client.close()
	#print response
	#print ""
	return response

def EchoClient(ServerHost, ServerPort):
	if ServerHost and ServerPort == "":
		ServerHost, ServerPort = "", 50007
	else:
		#print "TCP Echo Data"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
		try:
			s.bind((ServerHost, ServerPort))#開始監聽的IP與Port
			s.listen(1)#設定連線上限1個
		except socket.error, msg:
			print "ERROR: ", msg#顯示錯誤，
			s.close()
			s = None

		if s is None:#如果s = None
			sys.exit(1)#離開程式

		print "Listen of Host and Port: %s:%d"%(ServerHost, ServerPort)#Listen Host of ServerHost and ServerPort
		data_len = 0
		try:
			conn, addr = s.accept()#將sockt「網路介面」的資訊放入conn，遠端連線資訊存入addr
		except KeyboardInterrupt:
			print "Closing Connection"
			s.close()
			s = None
			sys.exit(1)
		s.close()
		AllList = [conn, addr, ServerHost, ServerPort]
		return AllList

def EchoData(conn, addr, ServerHost, ServerPort):
	if conn and addr == "":
		conn, addr = EchoClient()
	else:
		try:
			data = conn.recv(4096)#將EEG送來的資料存入date變數裡面
			#if not data:break

			date =  time.strftime("%Y/%m/%d %H:%M:%S")
			d = datetime.datetime.strptime(date, '%Y/%m/%d %H:%M:%S')
			date1 = time.mktime(d.timetuple()) + 1e-6 * d.microsecond

			ClientIP, ClientPort = addr
			print "Incoming connection accepted: " + str(ClientIP) + ":" + str(ClientPort)#Client of IP and Port

			print date, addr[0]#, ":", repr(data)#顯示時間、IP、Port、TCP資料
			print ""
			conn.send(data)
		except KeyboardInterrupt:
			#print "Closing Connection"
			s.close()
			s = None
			sys.exit(1)

		conn.close()
		ReprData = repr(data)
		AllList = [date1, ClientIP, ClientPort, ServerHost, ServerPort, ReprData]
		return AllList

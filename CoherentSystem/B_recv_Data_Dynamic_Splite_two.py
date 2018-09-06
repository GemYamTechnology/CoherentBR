#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# Derive from: recv_Laisan2
"""
201804211450可以將標記刪掉並條列00開頭010101結尾的字串
"""
from matplotlib import animation
import sys
import string
import time
import pandas
import csv
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
from cobs import cobs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

"""
--------------------------------------------------
24bit轉10bit模組
--------------------------------------------------
"""
def conv24bits (b1, b2, b3):
    ans = (b1  << 16) + (b2 << 8) + b3;
    ans = ans  if not (ans & 0x800000) else ans - 0x1000000
    return ans
"""
--------------------------------------------------
"""
"""
--------------------------------------------------
檔案創建
--------------------------------------------------
"""
#創建檔案結束
packet_count249=0#封包IP來源.249
packet_count252=0#封包IP來源.252
packet_count=1#封包IP
data = "recv_text.txt"#檔案位置

iparray=['249','252']#檔案命名的串列
for a in iparray:#檔案自動命名
    f1 = open(a + 'recv_text1.csv', 'w')
    f2 = open(a + 'recv_text2.csv', 'w')
    f3 = open(a + 'recv_text3.csv', 'w')
    f4 = open(a + 'recv_text4.csv', 'w')
    f5 = open(a + 'recv_text5.csv', 'w')
    f6 = open(a + 'recv_text6.csv', 'w')
    f7 = open(a + 'recv_text7.csv', 'w')
    f8 = open(a + 'recv_text8.csv', 'w')


f1.close()#創建檔案結束
f2.close()#創建檔案結束
f3.close()#創建檔案結束
f4.close()#創建檔案結束
f5.close()#創建檔案結束
f6.close()#創建檔案結束
f7.close()#創建檔案結束
f8.close()#創建檔案結束
"""
--------------------------------------------------
"""

c = []
with open(data, 'rb') as csvfile:#讀取資料
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    """
    --------------------------------------------------
    將逗點字串分割重新整理成無逗點字串
    --------------------------------------------------
    """
    for row in spamreader:
        a = ','.join(row)[33:1330]#拆分字串並加入逗點
        ip = str(row[4])#尋找第四段的IP

        #print a
        #print ''
        CommaString = a
        SplitString = CommaString.split(',')#利用逗點分割字串
        #print SplitString
        i = 0
        for u in SplitString:
            #if u == "'":
                #a = "a"
            if u == "00":#如果u是"00"
                i = i + 1
                BeforeDecoding = u
                #print BeforeDecoding
            else:
                i = i + 1
                if i > 1:
                    BeforeDecoding += u
                else:
                    BeforeDecoding = u
            #print BeforeDecoding
            if "010101" in BeforeDecoding:
                print BeforeDecoding
                # print ''
                """
                --------------------------------------------------
                """
                """
                --------------------------------------------------
                20180429, Laisan, Decode it by cobs
                解碼於COBS
                --------------------------------------------------
                """
                BeforeDecoding = BeforeDecoding.replace("'","")#解碼前將'更換成空值
                Decoding=""
                c=[]
                for x in range(0, len(BeforeDecoding), 2):
                    c.append(BeforeDecoding[x:x+2])
                c.pop(0) # Take out leading 00輸出00
                if len(c) == 34: # Must be one complete packet
                   try:
                      i=0
                      for u in c:#解碼中
                          a = int(u, base=16)
                          i = i+1
                          if i > 1:
                             Decoding += chr(a)
                          else:
                             Decoding = chr(a)
                      AfterDecoding = cobs.decode(Decoding[:])
                      i=0
                      output_str = ""
                      for u in AfterDecoding:
                          c = '{0:0{1}X}'.format(ord(u),2)
                          i = i+1
                          if i > 1:
                              output_str += c + " "
                          else:
                              output_str = c + " "
                      print "Packet #" + str(packet_count) + ": " + output_str
                      if ip == '192.168.0.249':
                          packet_count249+=1
                      elif ip == '192.168.0.252':
                          packet_count252+=1
                      for i in range(6,29,3):
                          a= conv24bits(ord(AfterDecoding[i]), ord(AfterDecoding[i+1]), ord(AfterDecoding[i+2]))
                          print a

                          if ip == '192.168.0.249':
                              if i == 6 :
                                  f1 = open('249recv_text1.csv', 'at+')
                                  f1.write(str(packet_count240) +','+ str(a) +'\n')
                                  f1.close()
                              elif i==9:
                                  f2 = open('249recv_text2.csv', 'at+')
                                  f2.write(str(packet_count240) +','+ str(a) +'\n')
                                  f2.close()
                              elif i==12:
                                  f3 = open('249recv_text3.csv', 'at+')
                                  f3.write(str(packet_count240) +','+ str(a) +'\n')
                                  f3.close()
                              elif i==15:
                                  f4 = open('249recv_text4.csv', 'at+')
                                  f4.write(str(packet_count240) +','+ str(a) +'\n')
                                  f4.close()
                              elif i==18:
                                  f5 = open('249recv_text5.csv', 'at+')
                                  f5.write(str(packet_count240) +','+ str(a) +'\n')
                                  f5.close()
                              elif i==21:
                                  f6 = open('249recv_text6.csv', 'at+')
                                  f6.write(str(packet_count240) +','+ str(a) +'\n')
                                  f6.close()
                              elif i==24:
                                  f7 = open('249recv_text7.csv', 'at+')
                                  f7.write(str(packet_count240) +','+ str(a) +'\n')
                                  f7.close()
                              elif i==27:
                                  f8 = open('249recv_text8.csv', 'at+')
                                  f8.write(str(packet_count240) +','+ str(a) +'\n')
                                  f8.close()
                          elif ip =='192.168.0.252':
                              if i == 6 :
                                  f1 = open('252recv_text1.csv', 'at+')
                                  f1.write(str(packet_count252) +','+ str(a) +'\n')
                                  f1.close()
                              elif i==9:
                                  f2 = open('252recv_text2.csv', 'at+')
                                  f2.write(str(packet_count252) +','+ str(a) +'\n')
                                  f2.close()
                              elif i==12:
                                  f3 = open('252recv_text3.csv', 'at+')
                                  f3.write(str(packet_count252) +','+ str(a) +'\n')
                                  f3.close()
                              elif i==15:
                                  f4 = open('252recv_text4.csv', 'at+')
                                  f4.write(str(packet_count252) +','+ str(a) +'\n')
                                  f4.close()
                              elif i==18:
                                  f5 = open('252recv_text5.csv', 'at+')
                                  f5.write(str(packet_count252) +','+ str(a) +'\n')
                                  f5.close()
                              elif i==21:
                                  f6 = open('252recv_text6.csv', 'at+')
                                  f6.write(str(packet_count252) +','+ str(a) +'\n')
                                  f6.close()
                              elif i==24:
                                  f7 = open('252recv_text7.csv', 'at+')
                                  f7.write(str(packet_count252) +','+ str(a) +'\n')
                                  f7.close()
                              elif i==27:
                                  f8 = open('252recv_text8.csv', 'at+')
                                  f8.write(str(packet_count252) +','+ str(a) +'\n')
                                  f8.close()
                      packet_count = packet_count + 1
                      plt.show()
                   except:
                      print "Packet #" + str(packet_count) + " could not be decoded.\n"

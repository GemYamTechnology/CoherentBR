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
def conv24bits(b1, b2, b3):
    ans = (b1 << 16) + (b2 << 8) + b3;
    ans = ans if not (ans & 0x800000) else ans - 0x1000000
    return ans

packet_count=1
data = "recv_text_long3_one.txt"#檔案位置
f1 = open('recv_text1.csv', 'w')
f2 = open('recv_text2.csv', 'w')
f3 = open('recv_text3.csv', 'w')
f4 = open('recv_text4.csv', 'w')
f5 = open('recv_text5.csv', 'w')
f6 = open('recv_text6.csv', 'w')
f7 = open('recv_text7.csv', 'w')
f8 = open('recv_text8.csv', 'w')


f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
f8.close()
c = []
with open(data, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        a = ','.join(row)[33:1330]
        
        #print a
        #print ''
        CommaString = a
        SplitString = CommaString.split(',')#分割字串
        #print SplitString
        i = 0
        for u in SplitString:
            #if u == "'":
                #a = "a"
            if u == "00":
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

                # 20180429, Laisan, Decode it by cobs
                BeforeDecoding = BeforeDecoding.replace("'","")
                Decoding=""
                c=[]
                for x in range(0, len(BeforeDecoding), 2):
                    c.append(BeforeDecoding[x:x+2])
                c.pop(0) # Take out leading 00
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
                      for i in range(6,29,3):
                          a= conv24bits(ord(AfterDecoding[i]), ord(AfterDecoding[i+1]), ord(AfterDecoding[i+2]))
                          print a
                          if i == 6 :
                              f1 = open('recv_text1.csv', 'at+')
                              f1.write(str(packet_count) +','+ str(a) +'\n')
                              f1.close()

                          elif i==9:
                              f2 = open('recv_text2.csv', 'at+')
                              f2.write(str(packet_count) +','+ str(a) +'\n')
                              f2.close()
                          elif i==12:
                              f3 = open('recv_text3.csv', 'at+')
                              f3.write(str(packet_count) +','+ str(a) +'\n')
                              f3.close()
                          elif i==15:
                              f4 = open('recv_text4.csv', 'at+')
                              f4.write(str(packet_count) +','+ str(a) +'\n')
                              f4.close()
                          elif i==18:
                              f5 = open('recv_text5.csv', 'at+')
                              f5.write(str(packet_count) +','+ str(a) +'\n')
                              f5.close()
                          elif i==21:
                              f6 = open('recv_text6.csv', 'at+')
                              f6.write(str(packet_count) +','+ str(a) +'\n')
                              f6.close()
                          elif i==24:
                              f7 = open('recv_text7.csv', 'at+')
                              f7.write(str(packet_count) +','+ str(a) +'\n')
                              f7.close()
                          elif i==27:
                              f8 = open('recv_text8.csv', 'at+')
                              f8.write(str(packet_count) +','+ str(a) +'\n')
                              f8.close() 
                      packet_count = packet_count + 1
                      plt.show()
                   except:
                      print "Packet #" + str(packet_count) + " could not be decoded.\n"
                

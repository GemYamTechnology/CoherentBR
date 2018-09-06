#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
"""
201804211450可以將標記刪掉並條列00開頭010101結尾的字串
"""
import sys
import time
import pandas
import csv
from cobs import cobs

def conv24bits(b1, b2, b3):
    ans = (b1 << 16) + (b2 << 8) + b3;
    ans = ans if not (ans & 0x800000) else ans - 0x1000000
    return ans

packet_count=1
data = "C:\\Users\\Gemyam\\Desktop\\Software_0429\\recv_text_long3_one.txt"#檔案位置
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
                          print conv24bits(ord(AfterDecoding[i]), ord(AfterDecoding[i+1]), ord(AfterDecoding[i+2]))
                      packet_count = packet_count + 1
                   except:
                      print "Packet #" + str(packet_count) + " could not be decoded.\n"

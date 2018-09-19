#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
import csv

def WriteCSV(FileName, Data):
    file = open(FileName, 'w')
    file.write(Data)
    file.close()#創建檔案結束

def CreateCSV(FileName):
    file = open(FileName, 'w')
    file.close()#創建檔案結束

def ReadNoDealWithCSV(FileName):
    with open(FileName, 'rb') as csvfile:#讀取資料
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    return spamreader

def ReadDealWithCSV(FileName):
    graph_data1 = open(FileName, 'r').read()
    lines1 = graph_data1.split('\n')
    return lines1

def aa(FileName, Data):#打開一個文件用於讀寫。如果該文件已存在，文件指針將會放在文件的結尾。文件打開時會是追加模式。如果該文件不存在，創建新文件用於讀寫。
    file = open(FileName, 'at+')
    file.write(Data)
    file.close()

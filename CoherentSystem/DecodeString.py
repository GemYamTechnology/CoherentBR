#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# Derive from: recv_Laisan2
"""
20180823 EEG封包解碼,24bit To 10bit,逗點去除
"""
from cobs import cobs

def conv24bits(b1, b2, b3):
    ans = (b1  << 16) + (b2 << 8) + b3;
    ans = ans  if not (ans & 0x800000) else ans - 0x1000000
    return ans

def RemoveCommas(String):
    RemovedCommasInTheString = []
    SplitString = String.split(',')#利用逗點分割字串
    i = 0
    for row in SplitString:
        if str(row) == "00":#如果u是"00"
            i = i + 1
            BeforeDecoding = row
        else:
            i = i + 1
            if i > 1:
                BeforeDecoding += row
            else:
                BeforeDecoding = row
        if "010101" in BeforeDecoding:
            if "010101" and "00" in BeforeDecoding:
                RemovedCommasInTheString.append(BeforeDecoding)
    #print RemovedCommasInTheString
    return RemovedCommasInTheString

def TCL(NoCommasStringList):#Two Character List
    for NoCommasString in NoCommasStringList:
        ListString = []
        for Quantity in range(0, len(NoCommasString), 2):#len()計算字串有多少字
            ListString.append(NoCommasString[Quantity:Quantity+2])
        ListString.pop(0)
        TwoCharacterQuantity = len(ListString)
    return TwoCharacterQuantity, ListString

def TCTDL(NoCommasStringList):#Two Character Two Dimensional List
    TwoDimensionalList = []
    TDLTCQ = []#Two Dimensional List Two Character Quantity
    for NoCommasString in NoCommasStringList:
        ListString = []
        for Quantity in range(0, len(NoCommasString), 2):#len()計算字串有多少字
            ListString.append(NoCommasString[Quantity:Quantity+2])
        ListString.pop(0)
        StringList = ListString#將00刪除
        TwoCharacterQuantity = len(ListString)
        TDLTCQ.append(TwoCharacterQuantity)
        TwoDimensionalList.append(StringList)
    return TDLTCQ, TwoDimensionalList

def DecodCOBS(TwoCharacterQuantity, TwoCharacterList):
    Decoding=""
    if TwoCharacterQuantity == 34: # Must be one complete packet
        try:
            i=0
            for row in TwoCharacterList:#解碼中
                a = int(row, base=16)
                i = i + 1
                if i > 1:
                    Decoding += chr(a)
                else:
                    Decoding = chr(a)
            AfterDecoding = cobs.decode(Decoding[:])
            """
            i=0
            output_str = ""
            for row in AfterDecoding:
                c = '{0:0{1}X}'.format(ord(row),2)
                i = i+1
                if i > 1:
                    output_str += c + " "
                else:
                    output_str = c + " "
            print "Packet: " + output_str
            """
        except:
            print "Packet could not be decoded.\n"
    return AfterDecoding

def DecimalConversion(AfterDecoding):#轉換進制的模組，利用conv24bit()來進行解碼
    DigitalList = []
    for i in range(6,29,3):
        Digital = conv24bits(ord(AfterDecoding[i]), ord(AfterDecoding[i+1]), ord(AfterDecoding[i+2]))
        DigitalList.append(Digital)
    return DigitalList

def RCTCLDCOBSDC(String):
    OutputList = []
    import DecodeString
    for NoCommasStringList in DecodeString.RemoveCommas(String):
        NoCommasStringList = [NoCommasStringList]
        TwoCharacterQuantity, TwoCharacterList = DecodeString.TCL(NoCommasStringList)
        TwoCharacterQuantity, TwoCharacterList = [TwoCharacterQuantity], [TwoCharacterList]
        for TCQ in TwoCharacterQuantity:
            for TCL in TwoCharacterList:
                AfterDecoding = DecodeString.DecodCOBS(TCQ, TCL)
                OutputList.append(DecodeString.DecimalConversion(AfterDecoding))
    return OutputList

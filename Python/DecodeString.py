#!/usr/bin/python
# -*- coding: utf-8 -*-
# coding = UTF-8
# Derive from: recv_Laisan2
"""
20180823 EEG封包解碼,24bit To 10bit,逗點去除
"""
from cobs import cobs
class Decode(object):
    """docstring for Decode."""
    def __init__(self, arg = "CoherentBR.0.1.201810100850"):
        super(Decode, self).__init__()
        self.arg = arg

    def conv24bits(self, b1, b2, b3):
        ans = (b1  << 16) + (b2 << 8) + b3;
        ans = ans  if not (ans & 0x800000) else ans - 0x1000000
        return ans

    def RemoveCommas(self, String):
        self.RemovedCommasInTheString = []
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
                    self.RemovedCommasInTheString.append(BeforeDecoding)
        return self.RemovedCommasInTheString

    def TCL(self, NoCommasStringList = self.RemovedCommasInTheString):#Two Character List
        for NoCommasString in NoCommasStringList:
            self.ListString = []
            for Quantity in range(0, len(NoCommasString), 2):#len()計算字串有多少字
                self.ListString.append(NoCommasString[Quantity:Quantity+2])
            self.ListString.pop(0)
            self.TwoCharacterQuantity = len(self.ListString)
        return self.TwoCharacterQuantity, self.ListString

    def TCTDL(self, NoCommasStringList = self.RemovedCommasInTheString):#Two Character Two Dimensional List
        self.TwoDimensionalList = []
        self.TDLTCQ = []#Two Dimensional List Two Character Quantity
        for NoCommasString in NoCommasStringList:
            self.ListString = []
            for Quantity in range(0, len(NoCommasString), 2):#len()計算字串有多少字
                self.ListString.append(NoCommasString[Quantity:Quantity+2])
            self.ListString.pop(0)
            StringList = self.ListString#將00刪除
            TwoCharacterQuantity = len(self.ListString)
            self.TDLTCQ.append(TwoCharacterQuantity)
            self.TwoDimensionalList.append(StringList)
        return self.TDLTCQ, self.TwoDimensionalList

    def DecodCOBS(self, TwoCharacterQuantity, TwoCharacterList):
        Decoding = ""
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
                self.AfterDecoding = cobs.decode(Decoding[:])
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
        return self.AfterDecoding

    def DecimalConversion(self, AfterDecoding = self.AfterDecoding):#轉換進制的模組，利用conv24bit()來進行解碼
        self.DigitalList = []
        for i in range(6,29,3):
            Digital = conv24bits(ord(AfterDecoding[i]), ord(AfterDecoding[i+1]), ord(AfterDecoding[i+2]))
            self.DigitalList.append(Digital)
        return self.DigitalList

    def RCTCLDCOBSDC(self, String):
        OutputList = []
        import DecodeString
        for NoCommasStringList in Decode.RemoveCommas(String):
            NoCommasStringList = [NoCommasStringList]
            TwoCharacterQuantity, TwoCharacterList = DecodeString.TCL(NoCommasStringList)
            TwoCharacterQuantity, TwoCharacterList = [TwoCharacterQuantity], [TwoCharacterList]
            for TCQ in TwoCharacterQuantity:
                for TCL in TwoCharacterList:
                    AfterDecoding = DecodeString.DecodCOBS(TCQ, TCL)
                    OutputList.append(DecodeString.DecimalConversion(AfterDecoding))
        return OutputList

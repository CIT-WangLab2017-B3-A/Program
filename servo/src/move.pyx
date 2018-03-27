#!/usr/bin/python
# coding: utf-8

# move module made of Hiroki Yumigeta
import sys, os.path
import serial
import time
from uart import *
class move(uart):
    def __init__(self, LEG_SERVOS=3, port='/dev/ttyS0', rate=115200):
        super(move, self).__init__(port, rate)
        self.LegServos = LEG_SERVOS
        self.Torque(0xFF, self.ON)
    def FileOpen(self, FileName=None):
        try:
            self.fp = open(FileName,'r')
            self.it = iter(self.fp.readline,'')# イテレータ
        except:
            return IOError
    def FileClose(self):
        self.fp.close()
    def DataImport(self):
        Data = []
        while True:
            try:
                line = self.it.next()# 1行ずつ読み取る
            except StopIteration:
                return None
            DataList = line[:-1].split(',')# 配列化
            # DataListの処理
            Group  = DataList[0]# Group
            fSpeed = DataList[1]# Speed
            for i in xrange(self.LegServos):
                VID    = [(3*int(Group)) + (i+1)]# ID
                fAngle = DataList[i+2]# 角度
                # float to int
                CtrData = self.Angle_Speed(fAngle, fSpeed)
                VID.extend(CtrData)
                Data.append(VID)# 2d array
            if DataList[-1] != ('&' or '&'+'\r'):# 配列の最後
                break
        return Data
    def Action(self, FileName, sleep):
        try:
            self.FileOpen('parameter/'+FileName)
            Data = self.DataImport()
            while Data != None:
                self.Write(self.LongPacket(self.ADDRESS_POS, Data))
                time.sleep(sleep)
                Data = self.DataImport()
            self.FileClose()
        except IOError:
            print 'File is not found'

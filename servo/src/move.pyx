#!/usr/bin/python
# coding: utf-8

# move module made of Hiroki Yumigeta
import sys, os.path
import serial
import time
from uart import *
class move(uart):
    def __init__(self, LEG_SERVOS=3, port='/dev/ttyS0', rate=115200):
        super().__init__(port, rate)
        self.LegServos = LEG_SERVOS
        self.Torque(0xFF, self.ON)
    def FileOpen(self, FileName=None):
        try:
            self.fp = open(FileName,'r')
            self.it = iter(fp.readline,'')# イテレータ
        except:
            return IOError
    def FileClose(self):
        try:
            self.fp.close()
    def DataImport(self):
        self.Data = []
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
                VID    = (3*int(Group)) + (i+1)# ID
                fAngle = DataList[i+2]# 角度
                # float to int
                [iAngle, iSpeed] = self.Angle_Speed(fAngle, fSpeed)
                self.Data.append([VID, iAngle, iSpeed])# 2d array
            if DataList[-1] != ('&' or '&'+'\r'):# 配列の最後
                break
        self.Data.pop(0)
        return self.Data
    def Action(self, FileName, sleep):
        try:
            self.FileOpen('parameter/'+FileName)
            self.Data = self.DataImport()
            while self.Data != None:
                self.Write(self.LongPacket(self.ADDRESS_POS, self.Data))
                time.sleep(sleep)
                self.Data = self.DataImport()
            self.FileClose()
        except IOError:
            print 'File is not found'

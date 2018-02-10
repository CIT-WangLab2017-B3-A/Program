#!/usr/bin/python
# coding: utf-8

# move module made of Hiroki Yumigeta
import sys, os.path
import serial
import time
from uart import uart
class move:
    def __init__(self, LEG_SERVOS=3, port='/dev/ttyS0', rate=115200):
        self.LegServos=LEG_SERVOS
        self.servo=uart(port, rate)
        self.servo.Torque(0xFF, self.servo.ON)
    def FileOpen(self, FileName=None):
        if FileName!=None:
            if os.path.isfile(FileName):
                self.fp = open(FileName,'r')
                self.flag = True
            else:
                self.flag = False
        else:
            self.flag = False
    def FileClose(self):
        if self.flag:
            self.fp.close()
            self.flag = False
    def DataImport(self):
        self.Data=[]
        if self.flag:
            while True:
                self.line = self.fp.readline()
                if not self.line:
                    self.flag = False
                    return None
                self.DataList = self.line[:-1].split(',')
                self.Group = int(self.DataList[0])
                self.Speed = self.DataList[1]
                for i in xrange(self.LegServos):
                    self.VID = (3*int(self.Group))+i+1
                    self.Angle = self.DataList[i+2]
                    #self.Speed
                    
                    self.TmpData=self.servo.Angle_Speed(self.Angle, self.Speed)
                    self.Data.append([self.VID, self.TmpData[0], self.TmpData[1]])
                if self.DataList[-1]!=('&' or '&'+'\r'):
                    break
            return self.Data
            
    def MakePacket(self, Data):
        self.TxData = self.servo.LongPacket(0x1E, Data)
        return self.TxData
    def Stand(self, FileName):
        self.FileOpen(FileName)
        self.Data = self.DataImport()
        self.servo.Write(self.MakePacket(self.Data))
        time.sleep(3.0)
        self.FileClose()
    def ahead(self, FileName, sleep):
        self.FileOpen('parameter/Ahead/'+FileName)
        self.Data = self.DataImport()
        while self.Data!=None:
            self.servo.Write(self.MakePacket(self.Data))
            time.sleep(sleep)
            self.Data = self.DataImport()
        self.FileClose()
        
    def Action(self, FileName, sleep):
        self.FileOpen('parameter/'+FileName)
        self.Data = self.DataImport()
        while self.Data!=None:
            self.servo.Write(self.MakePacket(self.Data))
            time.sleep(sleep)
            self.Data = self.DataImport()
        self.FileClose()
    def Stop(self):
        self.servo.Stop()
    def Close(self):
        self.servo.Close()
        

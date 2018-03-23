#!/usr/bin/python
# coding: utf-8

# urat module made of Hiroki Yumigeta
import sys
import serial
import time
class uart(object):
    def __init__(self, port='/dev/ttyS0', rate=115200):
        # torque mode
        self.OFF    = 0x00
        self.ON     = 0x01
        self.PANTCH = 0x02
        # open port
        self.uart=serial.Serial(port, rate)
    def Write(self, TxData):
        self.uart.write(TxData)
        time.sleep(0.06)
    def Angle_Speed(self, fAngle, fSpeed):
        Angle = int(10.0*float(fAngle))
        Speed = int(100.0*float(fSpeed))
        tmpData = [Angle, (Angle>>8), Speed, (Speed>>8)]
        self.Data = map(lambda x:x&0x00FF, tmpData)
        return self.Data
    def CheckSum(self, Data):
        self.check=0x00
        for x in Data:
            self.check ^= x
        return self.check
    def ShortPacket(self, ID, Flag, Address, Cnt, Data):
        # packet header
        self.TxData = [0xFA, 0xAF]
        if type(Data)==type([]): # array
            Length = len(Data)
            tmpData = [ID, Flag, Address, Length, Cnt]
            tmpData.extend(Data)
        elif type(Data)==type(None):# None data(ex.reboot)
            tmpData = [ID, Flag, Address, 0x00, Cnt]
        else: # not array
            Length = 0x01
            tmpData = [ID, Flag, Address, Length, Cnt]
            tmpData.append(Data)
        # checkSum
        tmpData.append(self.CheckSum(tmpData))
        self.TxData.extend(tmpData)
        return self.TxData
    def LongPacket(self, Address, Data):
        # packet header
        self.TxData = [0xFA, 0xAF]
        Length = len(Data[0])# data par servo
        Cnt = len(Data)# servos
        tmpData = [0x00, 0x00, Address, Length, Cnt]
        for x in xrange(Data):
            tmpData.extend(x)
        # checkSum
        tmpData.append(self.CheckSum(tmpData))
        self.TxData.extend(tmpData)
        return self.TxData
    #control func
    def Reboot(self, ID):
        self.TxData = self.ShortPacket(ID, 0x20, 0xFF, 0x00, None)
        self.Write(self.TxData)
    def RomWrite(self, ID):
        self.TxData = self.ShortPacket(ID, 0x40, 0xFF, 0x00, None)
        self.Write(self.TxData)
    def ChangeID(self, NewID):
        self.TxData = self.ShortPacket(0xFF, 0x00, 0x04, 0x01, NewID)
        self.Write(self.TxData)
        self.RomWrite(NewID)
        self.Reboot(NewID)
        print 'Finish!'
    def Inverse(self, ID, SW):
        self.TxData = self.ShortPacket(ID, 0x00, 0x05, 0x01, SW)
        self.Write(self.TxData)
        self.RomWrite(ID)
        self.Reboot(ID)
        print 'Finish!'
    def Torque(self, ID, SW):
        self.TxData = self.ShortPacket(ID, 0x00, 0x24, 0x01, SW)
        self.Write(self.TxData)
    def Start(self):
        self.Torque(0xFF, self.ON)
    def Stop(self):
        self.Torque(0xFF, self.PANTCH)
    def ZeroAll(self):
        self.Data = self.Angle_Speed(0, 0.01)
        self.Torque(0xFF, self.ON)
        self.TxData = self.ShortPacket(0xFF, 0x00, 0x1E, 0x01, self.Data)
        self.Write(self.TxData)
        time.sleep(2.0)
        self.Stop()
    def Tester(self,ID):
        self.Torque(ID, self.ON)
        for j in xrange(2):#two loop
            self.Data = self.Angle_Speed(30, 0.01)
            self.TxData = self.ShortPacket(ID, 0x00, 0x1E, 0x01, self.Data)
            self.Write(self.TxData)
            time.sleep(1.0)
            self.Data = self.Angle_Speed(0, 0.01)
            self.TxData = self.ShortPacket(ID, 0x00, 0x1E, 0x01, self.Data)
            self.Write(self.TxData)
            time.sleep(1.0)
        self.Torque(ID, self.OFF)
    def Close(self):
        self.Torque(0xFF,self.OFF)
        self.uart.close()
    def __del__(self):
        self.Torque(0xFF,self.OFF)
        self.uart.close()

#!/usr/bin/python
# coding: utf-8

from i2c import i2c
import Address
import time
import numpy as np
def d16(value):
    return -(value & 0x8000) | (value & 0x7FFF)

class sensor:
    def __init__(self):
        self.compass = i2c(0x1E, 0x01)
        self.ToF = i2c(0x29, 0x01)
        self.NA = np.array([0.0, 0.0, 0.0])
        self.NM = np.matrix([0.0, 0.0, 0.0])
        self.BA = np.array([0.0, 0.0, 0.0])
        self.BM = np.matrix([0.0, 0.0, 0.0])

    def SetData(self):
        self.BA = self.NA
        self.BM = self.NM
        for i in range(8):
            reg = 0x1F+i
            self.compass.write(reg, Address.CTRL[i])
            time.sleep(0.001)
        self.ax = float(d16(((self.compass.read(0x29)&0xFF)<<8) | (self.compass.read(0x28)&0xFF))) * 6.0 / 65535.0
        self.ay = float(d16(((self.compass.read(0x2B)&0xFF)<<8) | (self.compass.read(0x2A)&0xFF))) * 6.0 / 65535.0
        self.az = float(d16(((self.compass.read(0x2D)&0xFF)<<8) | (self.compass.read(0x2C)&0xFF))) * 6.0 / 65535.0
        self.mx = float(d16(((self.compass.read(0x09)&0xFF)<<8) | (self.compass.read(0x08)&0xFF))) * 4.0 / 65535.0
        self.my = float(d16(((self.compass.read(0x0B)&0xFF)<<8) | (self.compass.read(0x0A)&0xFF))) * 4.0 / 65535.0
        self.mz = float(d16(((self.compass.read(0x0D)&0xFF)<<8) | (self.compass.read(0x0C)&0xFF))) * 4.0 / 65535.0
        self.NA = np.array([-self.az, self.ax, -self.ay])
        self.NM = np.matrix([-self.mz, self.mx, -self.my])
        self.A = (self.NA+self.BA)*0.5
        self.M = (self.NM+self.BM)*0.5
        time.sleep(0.05)

    def OffsetWrite(self, FileName, DataMax):
        self.OffA = np.array([0.0, 0.0, 0.0])
        self.OffM = np.matrix([0.0, 0.0, 0.0])
        for i in xrange(DataMax):
            self.SetData()
            self.OffA += self.A
            self.OffM += self.M
        self.OffA = map(str, self.OffA / float(DataMax))
        self.OffM = map(str, self.OffM / float(DataMax))
        self.fp = open(FileName, "w")
        self.fp.write(self.OffA[0] + ", " + self.OffA[1] + ", " + self.OffA[2] + "\n")
        self.fp.write(self.OffM[0, 0] + ", " + self.OffM[0, 1] + ", "+self.OffM[0, 2])
        self.fp.close()

    def OffsetRead(self, FileName):
        self.fp = open(FileName, "r")
        self.line = self.fp.readline()
        self.OffA = map(float, np.array(self.line[:-1].split(',')))
        print self.OffA
        self.line = self.fp.readline()
        self.OffM = map(float, np.array(self.line[:-1].split(',')))
        print self.OffM
        self.fp.close()

    def Yaw(self):# Yaw axis
        self.num = -np.arccos(np.dot(self.A, self.OffA))
        self.den = np.linalg.norm(self.A)*np.linalg.norm(self.OffA)
        self.alpha = self.num / self.den
        self.cross = np.cross(self.A, self.OffA)
        self.n = self.cross / np.linalg.norm(self.cross)
        self.Mrot = np.matrix([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
        self.nxx = self.n[0] * self.n[0]
        self.nxy = self.n[0] * self.n[1]
        self.nxz = self.n[0] * self.n[2]
        self.nyy = self.n[1] * self.n[1]
        self.nyz = self.n[1] * self.n[2]
        self.nzx = self.n[2] * self.n[0]
        self.nzz = self.n[2] * self.n[2]
        self.SinAlpha = np.sin(self.alpha)
        self.CosAlpha = np.cos(self.alpha)
        self.Mrot[0, 0] = self.nxx * (1.0-self.CosAlpha) + self.CosAlpha
        self.Mrot[0, 1] = self.nxy * (1.0-self.CosAlpha) + self.n[2] * self.SinAlpha
        self.Mrot[0, 2] = self.nxz * (1.0-self.CosAlpha) + self.n[1] * self.SinAlpha
        self.Mrot[1, 0] = self.nxy * (1.0-self.CosAlpha) + self.n[2] * self.SinAlpha
        self.Mrot[1, 1] = self.nyy * (1.0-self.CosAlpha) + self.CosAlpha
        self.Mrot[1, 2] = self.nyz * (1.0-self.CosAlpha) + self.n[0] * self.SinAlpha
        self.Mrot[2, 0] = self.nzx * (1.0-self.CosAlpha) + self.n[1] * self.SinAlpha
        self.Mrot[2, 1] = self.nyz * (1.0-self.CosAlpha) + self.n[0] * self.SinAlpha
        self.Mrot[2, 2] = self.nzz * (1.0-self.CosAlpha) + self.CosAlpha
        self.MM = self.Mrot * self.M.T
        self.YawData = np.arctan2(self.MM[0], self.MM[1])
        return np.rad2deg(self.YawData)

    def ReadDistance(self): #ToF sensor module
        self.ToF.write(0x0000, 0x01)
        time.sleep(0.1)
        if self.ToF.res(0x0014, 100):
            self.data = self.ToF.read_block(0x0014, 12)
            self.distance = ((self.data[10]&0xff)<<8) | (self.data[11]&0xff)
            return self.distance

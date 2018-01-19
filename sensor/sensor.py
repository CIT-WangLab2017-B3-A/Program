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
        self.ToF = i2c(0x29, 0x01)

    def ReadDistance(self): #ToF sensor module
        self.ToF.write(0x0000, 0x01)
        time.sleep(0.1)
        if self.ToF.res(0x0014, 100):
            self.data = self.ToF.read_block(0x0014, 12)
            self.distance = ((self.data[10]&0xff)<<8) | (self.data[11]&0xff)
            return self.distance

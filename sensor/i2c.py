#!/usr/bin/python
# coding: utf-8

#i2c module made of Hiroki Yumigeta
import smbus
import time

class i2c:
    def __init__(self, address, port):
        self.address=address
        self.sensor=smbus.SMBus(port)
    def write(self, cmd, value):
        self.sensor.write_byte_data(self.address, cmd, value)
    def read(self, cmd):
        return self.sensor.read_byte_data(self.address, cmd)
    def read_block(self, cmd, byte):
        return self.sensor.read_i2c_block_data(self.address, cmd, byte)
    def res(self, cmd, timeout):
        for delay in range(timeout):
            val = self.read(cmd)
            if(val&0x01): return True
            time.sleep(0.001)
        return False
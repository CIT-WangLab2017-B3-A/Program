#!/usr/bin/python
# coding: utf-8

# LSM303D -3D compass (3D accelerometer & 3D magnetometer)
from sensor import sensor
import time
compass = sensor()
#compass.OffsetWrite("offset.csv",10000)
compass.OffsetRead("offset.csv")

for i in xrange(10000):
    compass.SetData()
    print "YAW: "+str(compass.Yaw())
    time.sleep(0.1)
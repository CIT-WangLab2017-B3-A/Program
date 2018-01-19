#!/usr/bin/python
# coding: utf-8

# VL53L0X -ToF sensor
from sensor import sensor
import time
ToF = sensor()

calib_x = [-18, -18, -19, -20, -33, -41, -29, -29, -28, -28]
LOOP = 10

Distance     = float(ToF.ReadDistance()) / float(LOOP)
Old_Distance = float(calib_x[int(Distance)/50])
while True:
    tmp = 0.0
    for i in xrange(LOOP):
        tmp += float(ToF.ReadDistance())
    Distance =  tmp / float(LOOP)
    Distance += float(calib_x[int(Distance)/50])
    print Distance
    Old_Distance = Distance
    time.sleep(0.001)

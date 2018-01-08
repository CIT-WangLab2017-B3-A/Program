#!/usr/bin/python
# coding: utf-8

# VL53L0X -ToF sensor

import wiringpi as w
from sensor import sensor
import time
ToF = sensor()
#ToF.OffsetRead("offset.csv")

for i in xrange(10000):
    print "Distance: "+str(ToF.ReadDistance())
    time.sleep(0.1)

#!/usr/bin/python
# coding: utf-8

# VL53L0X -ToF sensor
from sensor import sensor
import time

class ToF:
    def __init__(self):
        self.ToF = sensor()
    def ReadDistance(self):
        
        #calib_x = [-18, -18, -19, -20, -33, -41, -29, -29, -28, -28]
        LOOP = 10
        flag = 0
        tmp = 0.0
        for i in xrange(LOOP):
            tmp += float(self.ToF.ReadDistance())
        Distance =  tmp / float(LOOP)
        Distance = min(Distance, 499.0)
        #Distance += float(calib_x[int(Distance)/50])
        print Distance,
	if (Distance < 100):
	    flag = 2
	    print "ゲット"
	    return 2
        elif (Distance < 200):
            flag = 1
            print "Ballかも"
	    return 1
        else:
            flag = 0
            print "Ballない"
	    return 0
        time.sleep(0.001)

TOF = ToF()

TOF.ReadDistance()

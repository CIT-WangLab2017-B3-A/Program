#!/usr/bin/python
# coding: utf-8

# VL53L0X -ToF sensor
from sensor import sensor
import time
import csv

class ToF:
    def __init__(self):
        self.LOOP = 10
        self.ToF = sensor()
	self.old_Distance = [float(self.ToF.ReadDistance()) for i in xrange(self.LOOP-1)]

    def ReadDistance(self):
        #start = time.time()#time
        alpha = 0.25
        #LOOP = 10
        tmp = 0.0

        '''
        for i in xrange(LOOP):
            tmp += float(self.ToF.ReadDistance())
	'''
        tmp = float(self.ToF.ReadDistance())
	Distance = float(self.LOOP) * tmp
	for i in range(self.LOOP-1,1,-1):
	    Distance += float(i)*self.old_Distance[i-1]
	Distance /= sum(xrange(self.LOOP+1))
	for i in xrange(self.LOOP-2):
	    self.old_Distance[i] = self.old_Distance[i+1]
	self.old_Distance[self.LOOP-2] = Distance
        #Distance =  tmp / float(LOOP)
        
	'''
        Distance = min(Distance, 500.0)
	Distance = min(Distance, self.old_Distance*1.5)
	Distance = max(Distance, self.old_Distance*0.5)
	'''

	#RCフィルタ
        #Distance = Distance*alpha + self.old_Distance*(1.0-alpha)
	return Distance
	#self.old_Distance = Distance
	#print time.time()-start
if __name__ == '__main__':
    x=50
    target = [-15, -10, -5, 0, 5, 10, 15]
    TOF = ToF()
    with open('new_sens_Y_005.csv','w') as fp:
        CSV = csv.writer(fp,lineterminator='\n')
        for i in xrange(len(target)):
	    print "next",
	    print target[i]
	    time.sleep(5)
            error = x-TOF.ReadDistance()
	    CSV.writerow([target[i], error])
	    print error

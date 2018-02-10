#!/usr/bin/python
#coding:utf-8
import time
import wiringpi as wp

wp.wiringPiSetup()
wp.pinMode(21,1)
wp.digitalWrite(21,1)
time.sleep(2)
wp.digitalWrite(21,0)




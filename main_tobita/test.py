#!/usr/bin/python
# coding: utf-8

## model: Futaba RS304MD
## Temprate of move program

# import Library
from move import move
import time
import os

# main program
def main():
	print "test start!"
	servo = move()
	
	servo.Start()
	for i in xrange(4):
		for j in xrange(16):
			temp_str = "trot/test" + str(j) + ".csv"
			servo.Action(temp_str,0)
	'''
    for i in xrange(4):
		for j in xrange(16):
			temp_str = "carling/test" + str(15-j) + ".csv"
			servo.Action(temp_str,0)
    '''
	#servo.Close()
	print "end"

if __name__ == '__main__':
    while True:
        main()

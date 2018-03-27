#!/usr/bin/python
# coding: utf-8

## model: Futaba RS304MD
## Temprate of move program

# import Library
from move import move
import time

# main program
def main():
    servo = move()
    servo.Action('BallCatch.csv',1.0)
    
    for i in xrange(5):
    	'''
    	for i in xrange(8):
		temp_str = "walk08/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
	'''
    	'''
    	for i in xrange(12):
		temp_str = "walk12/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
	'''
    	'''
    	for i in xrange(16):
		temp_str = "walk16/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
        '''
        '''
    	for i in xrange(24):
		temp_str = "walk24/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
        '''
	'''
    	for i in xrange(24):
		temp_str = "walk24high/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
    	'''
	'''
    	for i in xrange(16):
		temp_str = "turn_right/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
	'''
	''''
    	for i in xrange(16):
		temp_str = "turn_left/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
	'''
    servo.Stop()
#    servo.Action('Ball/BallCatch.csv',0.55)
#    servo.Stop()
    #time.sleep(1.0)
#    servo.Action('Ball/BallDust.csv',0.55)
    time.sleep(1.0)
    servo.Close()

if __name__ == '__main__':
    main()

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
	print "demo start!"
	servo = move()
	
	servo.Start()
	servo.Action('poseing/pose2.csv',2)
	servo.Stop()

	servo.Start()
	servo.Action('Ball/BallCatch.csv',0.5)
	servo.Stop()
	time.sleep(1)
		
	servo.Start()
	for i in xrange(16):	
		temp_str = "stand_before_turn/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
	for i in xrange(1):
		for j in xrange(16):
			temp_str = "turn_right/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "turn_right/test" + str(15-j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(1):
		for j in xrange(16):
			temp_str = "turn_right/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	servo.Stop()

	servo.Start()
	for i in xrange(16):	
		temp_str = "stand_before_walk/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)

	for i in xrange(1):
		for j in xrange(24):
			temp_str = "walk24/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(1):
		for j in xrange(24):
			temp_str = "walk24/test" + str(23-j) + ".csv"
			servo.Action(temp_str,0.01)
	servo.Stop()
	time.sleep(0.5)

	servo.Start()
	for i in xrange(36):	
		temp_str = "high_stand_up/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
	for i in xrange(36):	
		temp_str = "high_stand_up/test" + str(36-i) + ".csv"
		servo.Action(temp_str,0.01)
	servo.Stop()

	servo.Start()
	for i in xrange(16):	
		temp_str = "stand_up_normal/test" + str(i) + ".csv"
		servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "motion_04/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "motion_02/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "motion_06/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "motion_05/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "motion_02/test" + str(15-j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "motion_07/test" + str(15-j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "motion_03/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(16):
			temp_str = "motion_03/test" + str(15-j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(1):
		for j in xrange(36):
			temp_str = "motion_01/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(1):
		for j in xrange(36):
			temp_str = "motion_01/test" + str(36-j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(18):
			temp_str = "motion_08/test" + str(j) + ".csv"
			servo.Action(temp_str,0.01)
	for i in xrange(2):
		for j in xrange(18):
			temp_str = "motion_08/test" + str(17-j) + ".csv"
			servo.Action(temp_str,0.01)
	servo.Stop()

	servo.Start()
	for i in xrange(16):	
		temp_str = "stand_up_normal/test" + str(16-i) + ".csv"
		servo.Action(temp_str,0.01)
	servo.Stop()
	'''	
	servo.Start()
	servo.Action('poseing/pose3.csv',0.5)
	servo.Stop()
	servo.Start()
	servo.Action('poseing/pose4.csv',0.5)
	servo.Stop()
	'''
	servo.Start()
	servo.Action('Ball/BallDust.csv',1.5)
	servo.Stop()
	
	servo.Start()
	servo.Action('poseing/pose0.csv',1.5)
	for i in xrange(16):	
		temp_str = "stand_up_normal/test" + str(15-i) + ".csv"
		servo.Action(temp_str,0.01)
	servo.Start()
	servo.Action('poseing/pose2.csv',2)
	servo.Close()
	os.system('sudo ./buzzer_demo famima')
	print "end"

if __name__ == '__main__':
	while True:
		main()

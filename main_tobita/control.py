#!/usr/bin/python

import math
import time
import socket
import sys
from move import move
from ToF import *

STEP_LENGTH = 204
STEP_ANGLE = 20 

class Soc_server:
	def __init__(self,address,port_number):
		self.host = address
		print self.host
		self.port = int(port_number) 
		self.serversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.serversock.bind((self.host,self.port))
		self.serversock.listen(10)
		print "Waiting for connections..."
		self.clientsock, self.client_address = self.serversock.accept()
		self.mode = 0
		self.control = Control()

	def main(self):
		while True:
			if self.mode == 0:
				print "Acceptance status"
				rcvmsg = self.clientsock.recv(1024)
				if rcvmsg == '':
					self.clientsock.close()
					break
				temp_data = rcvmsg.split(',')
				self.control.main((temp_data[0],float(temp_data[1])))
				if temp_data[0] == 'b':
					self.mode = 2
				else:
					self.mode = 1

			if self.mode == 1:
				print "send result"
				self.clientsock.sendall("0")
				self.mode = 0
			
			if self.mode == 2:
				fg = self.control.ball_check_fg
				print "send ball result",fg
				if fg == 1:
					self.clientsock.sendall("1")
				else:
					self.clientsock.sendall("0")
				self.mode = 0

class Control:
	def __init__(self):
		self.ball_check_fg = 0
		self.tof = ToF()

	def stand_up_before_walk(self):
		servo = move()
		for i in xrange(16):
			temp_str = 'stand_before_walk/test' + str(i) + '.csv'
			servo.Action(temp_str,0.01)
	
	def motion_01(self):
		servo = move()
		for i in xrange(36):
			temp_str = 'motion_01r/test' + str(i) + '.csv'
			servo.Action(temp_str,0.01)
	
	def stand_up_before_turn(self,direction):
		servo = move()
		for i in xrange(16):
			if direction == 'r':
				temp_str = 'stand_before_turn_right/test' + str(i) + '.csv'
			if direction == 'l':
				temp_str = 'stand_before_turn_left/test' + str(i) + '.csv'
			servo.Action(temp_str,0.01)
	
	def ahead(self,value):
		n = int(value // STEP_LENGTH) + 1
		servo = move()
		print "ahead :",value
		for i in xrange(n):
			for j in xrange(24):
				temp_str = 'walk24/test' + str(j) + '.csv'
				if i == (n - 1):
					if (value - ((n-1) * STEP_LENGTH)) < (STEP_LENGTH*j/24):
						break
				servo.Action(temp_str,0.01)
		servo.Close()
	
	def back(self,value):
		n = int(value // STEP_LENGTH) + 1
		servo = move()
		print "back :",value
		for i in xrange(n):
			for j in xrange(24):
				temp_str = 'back24/test' + str(j) + '.csv'
				if i == (n - 1):
					if (value - ((n-1) * STEP_LENGTH)) < (STEP_LENGTH*j/24):
						break
				servo.Action(temp_str,0.01)
		servo.Close()
	
	def high(self,value):
		n = int(value // STEP_LENGTH) + 1
		servo = move()
		print "high :",value
		for i in xrange(n):
			for j in xrange(24):
				temp_str = 'walk24high/test' + str(j) + '.csv'
				if i == (n - 1):
					if (value - ((n-1) * STEP_LENGTH)) < (STEP_LENGTH*j/24):
						break
				servo.Action(temp_str,0.01)
		servo.Close()

	def turn_right(self,value):
		n = int(value // STEP_ANGLE) + 1
		servo = move()
		print "right : ",value
		for i in xrange(n):
			for j in xrange(16):
				temp_str = 'turn_right/test' + str(j) + '.csv'
				if i == (n - 1):
					if (value - ((n-1) * STEP_ANGLE)) < (STEP_ANGLE*j/16):
						break
				servo.Action(temp_str,0.01)
		servo.Close()

	def turn_left(self,value):
		n = int(value // STEP_ANGLE) + 1
		servo = move()
		print "left : ",value
		for i in xrange(n):
			for j in xrange(16):
				temp_str = 'turn_left/test' + str(j) + '.csv'
				if i == (n - 1):
					if (value - ((n-1) * STEP_ANGLE)) < (STEP_ANGLE*j/16):
						break
				servo.Action(temp_str,0.01)
		servo.Close()

	def ball_catch(self):
		self.ball_check_fg = 0
		servo = move()
		servo.Action('Ball/BallCatch.csv',1.0)
		servo.Close()
		if self.tof.ReadDistance() == 2:
			self.ball_check_fg = 1
	
	def ball_dust(self):
		self.ball_check_fg = 0
		servo = move()
		#demo_action

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

		servo.Action('Ball/BallDust.csv',1.0)
		servo.Close()
	
	def main(self,action_data):
		print action_data
		if action_data[0] == 'b':
			self.ball_catch()
		if action_data[0] == 'm':
			self.motion_01()
		if action_data[0] == 'd':
			self.ball_dust()
		if action_data[0] == 'x':
			self.stand_up_before_walk()
			if action_data[1] > 0:
				self.ahead(1000 * action_data[1])
			else:
				self.back(1000 * -action_data[1])
		if action_data[0] == 'h':
			self.stand_up_before_walk()
			self.high(1000 * action_data[1])
		if action_data[0] == 'r':
			if action_data[1] > 0:
				self.stand_up_before_turn('l')
				self.turn_left(action_data[1])
			else:
				self.stand_up_before_turn('r')
				self.turn_right(-action_data[1])
		time.sleep(2)
		print "Move complete"

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 3:
		soc = Soc_server(args[1],args[2])
		soc.main()

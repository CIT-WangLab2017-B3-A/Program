#!/usr/bin/python

import math
import time
import socket
import sys
from move import move

STEP_LENGTH = 204
STEP_ANGLE = 15 

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
				self.mode = 1	
			if self.mode == 1:
				print "send result"
				self.clientsock.sendall("0")
				self.mode = 0

class Control:
	def __init__(self):
		pass

	def stand_up_before_walk(self):
		servo = move()
		for i in xrange(16):
			temp_str = 'stand_before_walk/test' + str(i) + '.csv'
			servo.Action(temp_str,0.01)
	
	def stand_up_before_turn(self):
		servo = move()
		for i in xrange(16):
			temp_str = 'stand_before_turn/test' + str(i) + '.csv'
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
	
	def dash(self,value):
		n = int(value // STEP_LENGTH) + 1
		servo = move()
		print "dash :",value
		for i in xrange(n):
			for j in xrange(8):
				temp_str = 'walk08/test' + str(j) + '.csv'
				if i == (n - 1):
					if (value - ((n-1) * STEP_LENGTH)) < (STEP_LENGTH*j/8):
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
		servo = move()
		servo.Action('Ball/BallCatch.csv',1.0)
		servo.Close()

	def main(self,action_data):
		print action_data
		if action_data[0] == 'b':
			self.ball_catch()
		if action_data[0] == 'x':
			self.stand_up_before_walk()
			self.ahead(1000 * action_data[1])
		if action_data[0] == 'd':
			self.stand_up_before_walk()
			self.dash(1000 * action_data[1])
		if action_data[0] == 'r':
			self.stand_up_before_turn()
			if action_data[1] > 0:
				self.turn_left(action_data[1])
			else:
				self.turn_right(-action_data[1])
		time.sleep(2)
		print "Move complete"

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 3:
		soc = Soc_server(args[1],args[2])
		soc.main()

#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import socket
import time

class Soc_client:
	def __init__(self, address,port_number):
		self.host = address
		self.port = int(port_number)
		self.mode = 0
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.client.connect((self.host,self.port))
		print "Connection success!"
		
	def main(self):
		try:
			while True:
				if self.mode == 0:
					#sdmsg = raw_input()
					sdmsg = "x,0.3"
					self.client.send(sdmsg)
					self.mode = 1
				if self.mode == 1:
					response = int(self.client.recv(4096))
					print "reslut",response
					self.mode = 0
		except KeyboardInterrupt:
			print "\nCtl+C"

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 3:
		c = Soc_client(args[1],args[2])
		c.main()


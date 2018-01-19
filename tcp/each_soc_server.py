#!/usr/bin/python

import sys
import time
import socket

class Soc_server:
	def __init__(self,address):
		self.host = address
		print self.host
		self.port = 002
		self.serversock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.mode = 0
		self.serversock.bind((self.host,self.port))
		self.serversock.listen(10)
		print "Waiting for connections..."
		self.clientsock, self.client_address = self.serversock.accept()

	def main(self):
		try:
			while True:
				if self.mode == 0:
					print "Acceptance status"
					rcvmsg = self.clientsock.recv(1024)
					if rcvmsg == '':
						self.clientsock.close()
						break
					print rcvmsg
					time.sleep(2)
					self.mode = 1
				if self.mode == 1:
					print "send result"
					self.clientsock.sendall("0")
					self.mode = 0
		except KeyboardInterrupt:
			print "\nCtl+C"

if __name__ == "__main__":
	args = sys.argv
	if len(args) == 2:
		s = Soc_server(args[1])
		s.main()

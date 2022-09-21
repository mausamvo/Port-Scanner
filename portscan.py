#!/usr/bin/python

import socket

#create the socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	#AF_INET explains i'm using ipv4 addr, STREAM explain i'm using TCP packets
socket.setdefaulttimeout(2) 					#expires in 2
#trying to perform a three-way handshake

host = raw_input("[*] Enter the host to scan: ")
port = int(raw_input("[*] Enter the port to scan: "))

def portscanner(port):
	if sock.connect_ex((host, port)): 			#we try to connect on this host amd port, but if error, port = closed
		print "Port %d is closed" % (port)
	else:
		print "Port %d is open" % (port)

portscanner(port)

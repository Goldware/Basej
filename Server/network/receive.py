import socket

def recv(s):
	msg = s.recv(1024)
	return msg

import socket

def init(ip, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((ip, port))
	s.listen(30)
	return s

def close(s):
	s.close()

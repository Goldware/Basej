import socket

def errCallback(s, errCode):
	s.send(errCode)

def successCallback(s):
	s.send(b's0')

def response(s, res):
	s.send(res)

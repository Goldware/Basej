import os

def isValid(req):

	# Verfication of dictionnary keys
	if req.has_key('request_id') and \
	   req.has_key('base') and \
	   req.has_key('cluster') and \
	   req.has_key('user') and \
	   req.has_key('password') and \
	   req.has_key('action') and \
	   req.has_key('values') or req.has_key('line'):

		return True
	else:
		return False

def isValidAuth(req, config_user, config_password):

	# Verfication of request authentication
	user = req.get('user')
	password = req.get('password')

	if user == config_user and password == config_password:
		return True
	else:
		return False

def isValidBase(req, listBase):

	base = req.get('base')
	if base in listBase:
		return True
	else:
		return False

def isValidCluster(req, listCluster):

	cluster = req.get('cluster')
	if cluster in listCluster:
		return True
	else:
		return False

def isValidValues(req, patternCluster):

	values = req.get('values')
	if len(values) == len(patternCluster):

		i = 0
		while i != len(values):
			if type(values[i]) != type(patternCluster[i]):
				return False
			else:
				i += 1

		return True
	else:
		return False

def isLineExist(base, cluster, line):

	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'r')
	clusterInstanceArray = clusterInstance.readlines()
	clusterInstance.close()

	if line <= len(clusterInstanceArray):
		return True
	else:
		return False

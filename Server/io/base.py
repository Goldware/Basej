import os, ast

def getListBase():

	listBase = open('base/list.json', 'r')
	content = listBase.read()
	listBase.close()

	listBase = ast.literal_eval(content)
	return listBase

def getListCluster(base):

	listCluster = open('base/' + base + '/list.json', 'r')
	content = listCluster.read()
	listCluster.close()

	listCluster = ast.literal_eval(content)
	return listCluster

def getPatternCluster(base, cluster):

	patternCluster = open('base/' + base + '/' + cluster + '/pattern.json', 'r')
	content = patternCluster.read()
	patternCluster.close()

	patternCluster = ast.literal_eval(content)
	return patternCluster

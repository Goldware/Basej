import os, json

def put(base, cluster, values):

	values = json.dumps(values)
	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'a+')
	clusterInstance.write(values + '\n')
	clusterInstance.close()

def get(base, cluster, line):

	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'r')
	clusterInstanceArray = clusterInstance.readlines()
	clusterInstance.close()

	data = clusterInstanceArray[line]
	return data

def dumpAll(base, cluster):

	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'r')
	clusterInstanceArray = clusterInstance.readlines()
	clusterInstanceArray = str(clusterInstanceArray)
	clusterInstance.close()

	return clusterInstanceArray

def edit(base, cluster, line, values):

	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'r')
	clusterInstanceArray = clusterInstance.readlines()
	clusterInstanceArray[line] = json.dumps(values) + '\n'
	clusterInstance.close()

	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'w')
	i = 0
	while i != len(clusterInstanceArray):
		clusterInstance.write(clusterInstanceArray[i])
		i += 1
	clusterInstance.close()

def delete(base, cluster, line):

	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'r')
	clusterInstanceArray = clusterInstance.readlines()

	try:
		clusterInstanceArray.remove(clusterInstanceArray[line])
	except:
		return False

	clusterInstance.close()

	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'w')
	i = 0
	while i != len(clusterInstanceArray):
		clusterInstance.write(clusterInstanceArray[i])
		i += 1

	clusterInstance.close()
	return True

def delAll(base, cluster):

	clusterInstance = open('base/' + base + '/' + cluster + '/values.json', 'w')
	clusterInstance.close()

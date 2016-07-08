import os
from datetime import datetime

def stock(client_ip, request_id, base, cluster, action):

	today = datetime.now()
	today_logFile = open('logs/logs/' + str(today.year) + str(today.month) + str(today.day) + '.log', 'a')
	line = '[' + str(today.hour) + ':' + str(today.minute) + ':' + str(today.second) + '] - ' + request_id + ' action=' + action + ' ip=' + client_ip + ' base=' + base + ' cluster=' + cluster

	today_logFile.write(line + '\n')
	today_logFile.close()

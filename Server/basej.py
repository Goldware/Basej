import config, ast, os, socket
import network.setup, network.receive, network.send
import io.base, io.cluster
import logs.manage
import request.handler

local_socket = network.setup.init(config.ip, config.port)

while True:
	remote_socket, info_connection = local_socket.accept()
	req = network.receive.recv(remote_socket)

	# Critical error in request handler
	try:
		req = ast.literal_eval(req)
	except:
		network.send.errCallback(remote_socket, 's6')
		continue

	print(req)

	# Request Validation
	if request.handler.isValid(req):

		request_id = req.get('request_id')
		base = req.get('base')
		cluster = req.get('cluster')
		action = req.get('action')

		if request.handler.isValidAuth(req, config.user, config.password):

			listBase = io.base.getListBase()
			if request.handler.isValidBase(req, listBase):

				listCluster = io.base.getListCluster(base)
				if request.handler.isValidCluster(req, listCluster):

					if action == 'PUT':

						patternCluster = io.base.getPatternCluster(base, cluster)
						if request.handler.isValidValues(req, patternCluster):
							network.send.successCallback(remote_socket)
							values = req.get('values')
							io.cluster.put(base, cluster, values)
						else:
							network.send.errCallback(remote_socket, 's5')
							continue

					elif action == 'GET':

						line = req.get('line')
						if line == 'ALL':
							grabbedCluster = io.cluster.dumpAll(base, cluster)
							network.send.response(remote_socket, grabbedCluster)
						else:

							try:
								line = int(line)
							except:
								network.send.errCallback(remote_socket, 's6')
								continue

							if request.handler.isLineExist(base, cluster, line) and not line < 0:
								value = io.cluster.get(base, cluster, line)
								network.send.response(remote_socket, value)
							else:
								network.send.errCallback(remote_socket, 's7')
								continue

					elif action == 'EDIT':

						line = int(req.get('line'))
						values = req.get('values')

						if request.handler.isLineExist(base, cluster, line) and not line < 0:

							patternCluster = io.base.getPatternCluster(base, cluster)
							if request.handler.isValidValues(req, patternCluster):
								io.cluster.edit(base, cluster, line, values)
								network.send.successCallback(remote_socket)
							else:
								network.send.errCallback(remote_socket, 's5')
								continue
						else:
							network.send.errCallback(remote_socket, 's7')
							continue

					elif action == 'DEL':

						line = req.get('line')
						if line == 'ALL':
							io.cluster.delAll(base, cluster)
							network.send.successCallback(remote_socket)
						else:

							try:
								line = int(line)
							except:
								network.send.errCallback(remote_socket, 's6')
								continue

							if request.handler.isLineExist(base, cluster, line) and not line < 0:
								if io.cluster.delete(base, cluster, line):
									network.send.successCallback(remote_socket)
								else:
									network.send.errCallback(remote_socket, 's7')
									continue
							else:
								network.send.errCallback(remote_socket, 's7')
								continue

					else:
						network.send.errCallback(remote_socket, 's8')
						continue
				else:
					network.send.errCallback(remote_socket, 's4')
					continue
			else:
				network.send.errCallback(remote_socket, 's3')
				continue
		else:
			network.send.errCallback(remote_socket, 's2')
			continue
	else:
		network.send.errCallback(remote_socket, 's1')
		continue

	# Log the request
	client_ip = str(info_connection[0])
	logs.manage.stock(client_ip, request_id, base, cluster, action)

# Socket close
network.setup.close(local_socket)

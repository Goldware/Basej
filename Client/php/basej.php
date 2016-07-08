<?php

class Basej {

	static $user;
	static $password;

	private function generateHash() {
		$a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890';
		$hash = str_shuffle($a);
		return $hash;
	}

	private function printError($errCode) {
		return $errCode;
	}

	function connect($ip, $user, $password, $port = 8044) {

		$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
		$result = socket_connect($socket, $ip, $port);

		Basej::$user = $user;
		Basej::$password = $password;

		return $socket;
	}

	function requestGET($socket, $base, $cluster, $line = 'ALL') {

		$request_id = Basej::generateHash();
		$request = "{
			'request_id' : '" . $request_id . "',
			'action' : 'GET',
			'base' : '" . $base . "',
			'cluster' : '" . $cluster . "',
			'user' : '" . Basej::$user . "',
			'password' : '" . Basej::$password . "',
			'line' : '" . $line . "'
		}";

		return $request;

	}

	function requestDEL($socket, $base, $cluster, $line) {

		$request_id = Basej::generateHash();
		$request = "{
			'request_id' : '" . $request_id . "',
			'action' : 'DEL',
			'base' : '" . $base . "',
			'cluster' : '" . $cluster . "',
			'user' : '" . Basej::$user . "',
			'password' : '" . Basej::$password . "',
			'line' : '" . $line . "'
		}";

		return $request;

	}

	function requestPUT($socket, $base, $cluster, $values) {

		$request_id = Basej::generateHash();
		$request = "{
			'request_id' : '" . $request_id . "',
			'action' : 'PUT',
			'base' : '" . $base . "',
			'cluster' : '" . $cluster . "',
			'user' : '" . Basej::$user . "',
			'password' : '" . Basej::$password . "',
			'values' : " . json_encode($values, JSON_UNESCAPED_UNICODE) . "
		}";

		return $request;

	}

	function requestEDIT($socket, $base, $cluster, $line, $values) {

		$request_id = Basej::generateHash();
		$request = "{
			'request_id' : '" . $request_id . "',
			'action' : 'EDIT',
			'base' : '" . $base . "',
			'cluster' : '" . $cluster . "',
			'user' : '" . Basej::$user . "',
			'password' : '" . Basej::$password . "',
			'line' : '" . $line . "',
			'values' : " . json_encode($values, JSON_UNESCAPED_UNICODE) . "
			}";

		return $request;

	}

	function submit($socket, $request) {
		socket_write($socket, $request, strlen($request));
		$callback = socket_read($socket, 1024);
		return $callback;
	}

}

?>

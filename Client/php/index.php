<?php

include('basej.php');
$Basej = new Basej;

$socket = $Basej->connect('127.0.0.1', 'root', 'toor');
$request = $Basej->requestGET($socket, 'test', 'test_cluster');
$callback = $Basej->submit($socket, $request);
$username = $Basej->getWhere($callback, 0, 'username');

?>

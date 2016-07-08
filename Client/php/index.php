<?php

include('basej.php');
$Basej = new Basej;

$socket = $Basej->connect('127.0.0.1', 'root', 'toor', 8044);
$request = $Basej->requestGET($socket, 'test', 'test_cluster');
$callback = $Basej->submit($socket, $request);

echo $callback;

?>

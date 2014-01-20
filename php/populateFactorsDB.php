<?php
include "functions.php";
$MIN=3;
$MAX=10000;

$t0 = microtime(true);
populateFactorizationsDB($MIN, $MAX);
echo "Time elapsed: ". (microtime(true) - $t0);

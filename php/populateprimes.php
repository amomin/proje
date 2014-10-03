<?php
include "functions.php";
$t0 = microtime(true);
populatePrimesDB(9999);
echo "Time elapsed: ". (microtime(true) - $t0);
//

/*
 * TESTS
$MIN = 50000;
$MAX = 60000;
$STEP = 2000;
$primes=array();
for ($x=$MIN; $x<$MAX; $x+=$STEP){
	$t0 = microtime(true);
	$primes = getPrimesMiller($x);
	$c = count($primes);
	echo "\nTime to get $x * 100 ($c many) primes using Miller: ". (microtime(true) - $t0);
//print_r($primes);
}
$primes=array();
for ($x=$MIN; $x<$MAX; $x+=$STEP){
	$t0 = microtime(true);
	$primes = getPrimesSieve($x);
	$c = count($primes);
	echo "\nTime to get $x * 100 ($c many) primes using Sieve: ". (microtime(true) - $t0);
//print_r($primes);
}
**/

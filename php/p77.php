<?php
include "functions.php";
$solns = array();

$_N=70;
$N=76;

$_COUNTWAYS=array(0=>1,1=>0);

function countWays($n, $maxtouse){
	global $_COUNTWAYS;

	if (isset($_COUNTWAYS[$n][$maxtouse])) return $_COUNTWAYS[$n][$maxtouse];
	if ($n==0) {
		//echo "0\n";
			return 1;
	}
	if ($n==1){
		//echo " XXX\n";
		return 0;
	}

	$primes = getPrimesDB($maxtouse);

	$count = 0;	
	foreach ($primes as $p){
		//echo "$p + ";
		$add = countWays($n-$p, min($n-$p,$p));
		$count += $add;
		//echo "\n";
	}
	//echo "Result for $n is $count\n";
	if (! isset($_COUNTWAYS[$n])) {
		$_COUNTWAYS[$n]=array();
		if (! isset($_COUNTWAYS[$n][$maxtouse])) {
			$_COUNTWAYS[$n][$maxtouse] = $count;
		}
	}
	return $count;	
}
for($n=$_N;$n<$N;$n++){
	$count = countWays($n,$n);
	echo "Result for $n is $count\n";
}


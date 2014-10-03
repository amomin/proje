<?php
include "functions.php";
$n=12354;

$primes = getPrimesFromDB($n);

$count = count($primes);
$result = array();
for ($i=0;$i<$count;$i++){
	$p = $primes[$i];
	//echo "<br>Prime is: $p.  ";
	$sum = 0;
	$k = floatval($n)/floatval($p);
	while ($k > 1){
		$sum += floor($k);
		$k/=$p;
	}
	//echo "It goes into $n! this many times: $sum";
	$result[$p] = $sum;
}

echo "<PRE>";
print_r($result);
echo "</PRE>";

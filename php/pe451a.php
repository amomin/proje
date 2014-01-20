<?php

$ans = array();
$N = 100;

for ($k=3; $k<$N; $k++){
	$found = false;
	$x = $k-2;
	while ($x >= 1 && !$found){
		if (( ($x * $x) % $k ) == 1){
			$ans[$k]=$x;
			$found = true;
		}
		$x-=1;
	}	
}
print_r($ans);

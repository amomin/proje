<?
/**
 * Problems:  
 * The answer for a power is not necessarily 1
 * You may have to consider all prime factors
 */
$N = 105;

// Compute answer 1
$t0 = time();
$ans = answer1($N);
for($i=3;$i < $N; $i+=2){
	echo "\nAns1 for $i: ".implode(',',$ans[$i]);
}
echo "\nTime: ".(time() - $t0);

/*
$i = 3*5*7;
echo "\nAns1 for $i: ".implode(',',$ans[$i]);
$i = 3*5*7*11;
echo "\nAns1 for $i: ".implode(',',$ans[$i]);
$i = 3*5*7*13;
echo "\nAns1 for $i: ".implode(',',$ans[$i]);
$i = 3*5*7*11*13;
echo "\nAns1 for $i: ".implode(',',$ans[$i]);
/*
 * For debugging, compare to a simpler answer 2
$ans2 = answer2($N);
for($i=3; $i < $N; $i+=2){
	if ($ans[$i] != $ans2[$i]){
		echo "DIFFERENT!";
		echo "\nAns1 for $i: ".implode(',',$ans[$i]);
	}
	echo "\nAns2 for $i: ".implode(',',$ans2[$i]);
}
*/
function answer1($N){
	$ans = array();
	// Fill in the powers of three
	$x=3;
	while($x < $N){
		$ans[$x] = array(1,$x-1);
		$x *= 3;
	}
	for ($x=5; $x<$N; $x+=2){
		if (! isset($ans[$x])){ //$x is prime
			$y=$x;
			$newans = array($x=>array(1,$x-1));
			while($y < $N){
				addNewSolutions($y, $ans, $newans, $N);
				$y *= $x;
			}
			$ans = $ans + $newans;
			ksort($ans);
		}
	}
	return $ans;
}
function addNewSolutions($p, $old, &$new, $limit){
	foreach ($old as $k=>$solns){ // each element of $solns is a solution for $k
		if ( $k * $p > $limit){
			return;
		}
		$c = count($solns)/2;
		if (2*$k < $c*$p){ // use $p instead of $k
			$newones=array();
			for ($l = 0; $l< $k; $l++){
				if (( pow($p * $l + 1, 2) % ($k*$p) )== 1){
					$newones[] = $p*$l + 1;
				}
				if (( pow($p * $l + ($p-1), 2) % ($k*$p) )== 1){
					$newones[] = $p*$l + ($p-1);
				}
			}
		}else{
			$newones=array();
			for ($l = 0; $l< $p; $l++){
				foreach ( $solns as $sol){
					if (( pow($k * $l + $sol, 2) % $p )== 1){ //Equivalently, by CRT, to if (( pow($k * $l + $sol, 2) % ($k * $p) )== 1){
						$newones[] = $k*$l + $sol;
						//echo "\n($k*$l+$sol)^2=". (pow($k*$l + $sol,2) % ($k * $p)) . " mod ($k * $p)\n";
					}
				}
			}
		}
		//echo "\n$k * $p =".$k*$p . " has solutions " . implode(',',$newones)."\n";
		$new[$k*$p] = $newones;
	}
}


// compute anser two
//
function answer2($N){
	$ans2 = array();
	for ($k=3; $k<$N; $k++){
		$x = 1;
		$ans2[$k] = array();
		while ($x <= $k-1){
			if (( ($x * $x) % $k ) == 1){
				$ans2[$k][]=$x;
			}
			$x+=1;
		}	
	}
	return $ans2;
}

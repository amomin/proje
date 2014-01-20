<?
/**
 * Problems:  
 * The answer for a power is not necessarily 1
 * You may have to consider all prime factors
 */
$ans = array();
$N = 1005;
$x=2;
function sqmod($i, $n){
	return ($i*$i) % $n;
}
function maxroot($p,$k){
	$max = 1;
	$i = $p*intval($k/$p/2);
	while ($i < $k-2){
		if (sqmod($i + 1, $k) == 1){
			$max = $i + 1;
		}else if (sqmod($i-1, $k) == 1){
			$max = $i - 1;
		}
		$i += $p;
	}
	return $max;
}
function gcd($a,$b){
	return ($a % $b)?gcd($b, $a % $b):$b;
}
$t1 = time();
$x=2;
$k=1;
$pows = array();
while (pow($x,$k)  < $N){
	$ans[pow($x,$k)] = 1;
	array_unshift($pows,pow($x,$k));
	$k+=1;
}
foreach ($pows as $x){
	fillin($x,$N,$ans);
}
$x=3;
$k=1;
$pows = array();
while (pow($x,$k)  < $N){
	$ans[pow($x,$k)] = 1;
	array_unshift($pows,pow($x,$k));
	$k+=1;
}
foreach ($pows as $x){
	fillin($x,$N,$ans);
}
for ($x=2; $x < $N; $x++){
	if (! isset($ans[$x])){ //$x is prime
		$k=1;
		$ans[$x]=1; //$x prime
		$pows = array();
		while (pow($x,$k)  < $N){
			$ans[pow($x,$k)] = 1; //for each power of a prime, $ans=1;
			array_unshift($pows,pow($x,$k));
			$k+=1;
		}
		print_r($pows);
		//foreach ($pows as $x){
		//}
		fillin($x,$N,$ans);
	}
}

function fillin($x, $N, &$ans){
	$l = $x + 1;
	while ($l*$x < $N){
		echo "\n$l, $x, gcd: ".gcd($l,$x);
		if (gcd($l,$x) == 1){
			if (! isset($ans[$l*$x])){
				$answ= maxroot($l, $l*$x, $N);
				$ans[$l*$x] = $answ;
			}
		}
		$l += 1;
	}
}
ksort($ans);
//print_r($ans);

$ans2 = array();

for ($k=3; $k<$N; $k++){
	$found = false;
	$x = $k-2;
	while ($x >= 1 && !$found){
		if (( ($x * $x) % $k ) == 1){
			$ans2[$k]=$x;
			$found = true;
		}
		$x-=1;
	}	
}

for ($i=3;$i<$N; $i+=2){
	echo "Method 1 vs method 2 for $i: ". $ans[$i]. ", ".$ans2[$i] . (($ans[$i] != $ans2[$i])?" DIFFERENT":"")."\n";
}

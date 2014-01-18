<?

$ans = array();
$N = 100000;
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

$t1 = time();
$x=2;
$k=1;
while (pow($x,$k)  < $N){
	$ans[pow($x,$k)] = 1;
	$k+=1;
}
$x=3;
$k=1;
while (pow($x,$k)  < $N){
	$ans[pow($x,$k)] = 1;
	$k+=1;
}
for ($x=2; $x < sqrt($N); $x++){
	if (! isset($ans[$x])){
		$k=1;
		$ans[$x]=1; //$x prime
		while (pow($x,$k)  < $N){
			$ans[pow($x,$k)] = 1; //for each power of a prime, $ans=1;
			$k+=1;
		}
	}
	$l = $x;
	while ($l*$x < $N){
		if (! isset($ans[$l*$x])){
			$answ= maxroot($l, $l*$x, $N);
			$ans[$l*$x] = $answ;
		}
		$l += 1;
	}
}
//ksort($ans);
//print_r($ans);

echo "Time: ". (time() - $t1) . "\n";
echo "SUM: ". array_sum($ans);

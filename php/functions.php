<?php

function gcd($a,$b){
	return ($a % $b)?gcd($b, $a % $b):$b;
}

function is_prime($n){
	if ($n == 2 || $n == 3) return true;
	$d = $n % 6;
	if (($d!=1 && $d!=5) || ($d == 0)){
		return false;
	}else{
		$k = min($n-1,15);
		return MillerPrimetest($n,$k);
	}
}
function primepowerfactorize($n){
	if (is_prime($n)){
		return array(array($n,1));
	}
	$x=2;
	$factors = array();
	while ($n > 1){
		if (($n % $x) == 0){
			$k=1;
			$n/=$x;
			while 	(($n % $x) == 0){
				$n/=$x;
				$k+=1;	
			}
			$factors[] = array("prime"=>$x, "power"=>$k);

		}
		$x++;
	}
	return $factors;	
}
function getPrimes($MAX){
	//return getPrimesSieve($MAX);
	return getPrimesMiller($MAX);
}
// Use the Miller test to get primes
function getPrimesMiller($MAX, $MIN=2){
	$primes = array();
	for($x=$MIN; $x<=$MAX; $x++){
		if (is_prime($x)){
			$primes[]=$x;
		}
	}
	return $primes;
}
function getPrimesDB($MAX){
	try{
		$DBO = new PDO("mysql:host=localhost;dbname=numbers", "public","");
		$DBO->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$QUERY=$DBO->prepare("SELECT * FROM primes WHERE value<=$MAX");
		$QUERY->execute();
		$DBO=null;
		//return $QUERY->fetchAll( PDO::FETCH_ASSOC);
		return $QUERY->fetchAll( PDO::FETCH_COLUMN);
	}catch(Exception $e){
		echo $e->getMessage();
	}

}
// Use a sieve method to generate primes
function getPrimesSieve($MAX){
	$nums = array();
	for ($x=2;$x< ceil($MAX); $x++){
		if (!in_array($x, $nums)){
			$primes[]=$x;
			$y=$x*$x;
			while ($y < $MAX){
				$nums[]=$y;
				$y+=$x;
			}
		}
	}
	return $primes;
}
function getPrimesFromDB($n){
	$query = "select value from primes where value<?";
	$values=array($n);
	try{
		$DBO = new PDO("mysql:host=localhost;dbname=numbers", "numbers","numbers");
		$DBO->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$QUERY=$DBO->prepare($query);
		$QUERY->execute($values);
		$result = $QUERY->fetchAll();
		$DBO=null;
	}catch(Exception $e){
		echo $e->getMessage();
	}
	$result = array_map (function($v){return $v['value'];}, $result);
	return $result;
}
function populateFactorizationsDB($MIN, $MAX){
	//$factorizations = array();
	$qMarray = array();
	$values = array();
	for($x=$MIN; $x<=$MAX; $x++){
		if (! is_prime($x)){
			$factorization = primepowerfactorize($x);
			foreach ($factorization as $factor){
				$values[]=$x;
				$values[]=$factor["prime"];
				$values[]=$factor["power"];
				$qMarray[] = "(?,?,?)";
			}
		}
	}
	$qmarks = implode(',',$qMarray);
	$query = "INSERT INTO factors(number,prime,power) VALUES $qmarks";
	try{
		$DBO = new PDO("mysql:host=localhost;dbname=numbers", "numbers","numbers");
		$DBO->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$QUERY=$DBO->prepare("delete from primes");
		$QUERY->execute();
		$QUERY=$DBO->prepare($query);
		$QUERY->execute($values);
		$DBO=null;
	}catch(Exception $e){
		echo $e->getMessage();
	}

}
function populatePrimesDB($MAX){
	$values = getPrimes($MAX);
	$questionmarks = '(?)';
	$count = count($values);
	for($i=1;$i<$count;$i++){
		$questionmarks.=',(?)';
	}
	$query = "INSERT INTO primes(value) values $questionmarks";
	try{
		$DBO = new PDO("mysql:host=localhost;dbname=numbers", "numbers","numbers");
		$DBO->setAttribute( PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$QUERY=$DBO->prepare("delete from primes");
		$QUERY->execute();
		$QUERY=$DBO->prepare($query);
		$QUERY->execute($values);
		$DBO=null;
	}catch(Exception $e){
		echo $e->getMessage();
	}
}
/*
 * Taken from rosettacode.org
 */
function MillerPrimeTest($n, $k) {
    if ($n == 2)
        return true;
    if ($n < 2 || $n % 2 == 0)
        return false;
 
    $d = $n - 1;
    $s = 0;
 
    while ($d % 2 == 0) {
        $d /= 2;
        $s++;
    }
 
    for ($i = 0; $i < $k; $i++) {
        $a = rand(2, $n-1);
 
        $x = bcpowmod($a, $d, $n);
        if ($x == 1 || $x == $n-1)
            continue;
 
        for ($j = 1; $j < $s; $j++) {
            $x = bcmod(bcmul($x, $x), $n);
            if ($x == 1)
                return false;
            if ($x == $n-1)
                continue 2;
        }
        return false;
    }
    return true;
}
/* Generate permutations from an array */
function permutations($n, $available=array(0,1,2,3,4,5,6,7,8,9)){
	if ($n==0){
		return array(array());
	}
	$solns=array();
	foreach ($available as $k=>$v){
		$a = $available;
		unset($a[$k]);
		$perms = permutations($n-1,$a);
		foreach ($perms as $p){
				$soln = array_merge(array($v),$p);
			$solns[] = $soln;
		}
	}
	return $solns;
}

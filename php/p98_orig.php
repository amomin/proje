<?php

function isSquare($x){
	$s = intval(sqrt($x));
	if ($s*$s==$x) return true;
	else return false;	
}

$fh = fopen("files/words.txt",'r');
$arr = fgetcsv($fh);
fclose($fh);

$sets = array();

foreach ($arr as $k=>$v){
		$split = str_split($v);
		sort($split);
		$alpha = implode($split);
		if (! isset($sets[$alpha])) $sets[$alpha]=array();
		$sets[$alpha][]=$v;
}

//echo "Total sets:"; echo count($sets);
foreach ($sets as $k=>$s){
	if (count($s)>1){
	}
	else{
		unset($sets[$k]);
	}
}
uksort($sets, 
	//"compLength" 
	//function compLength($x,$y){
	function ($x,$y){
		if (strlen($x)>strlen($y)) {
				return 1;
		}else if (strlen($x)<strlen($y)) {
				return -1;
		}else return 0;
	}

);
echo "Anagram sets:"; echo count($sets);
print_r($sets);
exit;
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
$len=0;
$perms = permutations(0);

$largest = 0;
foreach ($sets as $k=>$s){
	if ($len!=strlen($k)){
		$len=strlen($k);
		$perms=permutations($len);	
	}
	/*
	if ($len >3){
		break;
	}
	 */
	$patterns = str_split($k);
	foreach($perms as $p){
		$replacements=$p;
		$squares = array();
		foreach($s as $word){
			$res = str_replace($patterns,$replacements,$word);
			//print_r($res);
			$res = intval($res);
			if (($res>= pow(10,$len-1))){
				if (isSquare($res)){
					$squares[]=$res;
					//echo "Orig: $word, replacement $res\n";
				}			
			}
		}
		if (count($squares)>1){
			//print_r($squares);
			foreach($squares as $sq){
				if ($sq>$largest){
					$largest=$sq;
				}
			}
		}
	}
}
echo "Largest found is $largest";

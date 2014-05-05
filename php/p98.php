<?php

/* Strategy:
 * Find all known k-digit squares
 * substitute those for the first word in each set
 * and then see if the re-arragnements are squres
 *
 * This avoids looping through permutations
 */
function isSquare($x){
	$s = intval(sqrt($x));
	if ($s*$s==$x) return true;
	else return false;	
}

function numDigits($x){
	$res=0;
	while ($x>=1){
		$res++;
		$x/=10;
	}
	return $res;
}
/*  E.g. Need to test that we don't sub 7 for both 'O' and 'R', say
 */
function replacementOK($word,$nums){
	if (strlen($word)!==strlen("$nums")) return false;
	$arr= array();
	foreach (str_split("$nums") as $k=>$v){
		if(!isset($arr[$v])) $arr[$v]=$word[$k];
		else if ($arr[$v] != $word[$k]){
			return false;
		}
	}	
	return true;
}

/**
 * Read the file, and sort into sets of anagrams
 */
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
foreach ($sets as $k=>$s){
	if (count($s)>1){
	}
	else{
		unset($sets[$k]);
	}
}
uksort($sets, 
	function ($x,$y){
		if (strlen($x)>strlen($y)) {
				return 1;
		}else if (strlen($x)<strlen($y)) {
				return -1;
		}else return 0;
	}

);


/* Tables of squares of given number of digits
 */
$sq_len = array(2=>array(), 3=>array(), 4=>array(),5=>array(),6=>array(),7=>array(),8=>array(),9=>array());
$i=4;
$size=numDigits($i*$i);
while($size < 10){
	$sq_len[$size][]=$i*$i;
	$i+=1;
	$size=numDigits($i*$i);
}

/**Main**/
$len=0;
$largest = 0;
$largest_word = "";	
foreach ($sets as $k=>$s){
	if ($len!=strlen($k)){
		$len=strlen($k);
	}
	foreach($sq_len[$len] as $p){
		/* Try replacing the digits of the first word with the current square */
		$word = $s[0];
		$replacements=str_split("$p");
		/* But only proceed if the substitution is legal */
		if (replacementOK($word,"$p")){
			$squares = array();
			$patterns = str_split($word);
			foreach($s as $word){
				$res = str_replace($patterns,$replacements,$word);
				$res = intval($res);
				if ((numDigits($res) == $len)){ //Don't use if it starts with 0
					/* If it's a square, it's a candidate solution */
					if (isSquare($res) && ! in_array($res,$squares)){
						$squares[]=$res;
					}			
				}
			}
			/* If we have at least 2 candidates, then we can check them */
			if (count($squares)>1){
				foreach($squares as $sq){
					if ($sq>$largest){
						$largest=$sq;
						$largest_word = implode(',',$s);
					}
				}
			}
		}
	}
}
echo "Largest found is $largest, in one of $largest_word\n";

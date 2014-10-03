<?php
include "functions.php";

/* Note that in fact, you need only check the
 * the case where
 * $inner = (1,2,3,4,5)
 * $outer = (6,7,8,9,10)
 *
 * Certainly 10 must be on the outside to have 16 digits instead of 17 as stipulated,
 * and it is very plausible that a solution as such exists.  Thus one only needs
 * to find it, which is fairly trivial.
 *
 * Nonetheless it was an ok exercise to write out the loop of permutations (although
 * I originally built it because of a mistake in writing out the string was printing
 * the answer incorrectly (digits in the wrong order), so I implemented the full 
 * method as a sanity check before discovering my mistake.
 */

$set = array(1,2,3,4,5,6,7,8,9);

$innerSet = permutations(5,$set);

//$inner = array(1,2,4,5,6);
//$outer = array(7,8,9,10);
//$minouter = 3;

$maxsofar=0;

foreach ($innerSet as $inner){
	$minouter=0;
	$outer=array(10);
	foreach($set as $s){
		if (! in_array($s,$inner)){
			if($minouter==0){	
				$minouter=$s;
			}else{
				$outer[]=$s;
			}
		}

	}
	$res = test($minouter,$inner,$outer);
	if ($res!=null){
		if (intval($res) > $maxsofar){
				echo "New max so far of $res\n";
			$maxsofar=intval($res);
		}
	}
}

function test($minouter,$inner,$outer){
	$innerP = permutations(5,$inner);
	$outerP = permutations(4,$outer);

	foreach ($innerP as $i){
		foreach ($outerP as $o){
			array_unshift($o,$minouter);
			$sum = array();
			$sum[] = $i[0] + $i[1] + $o[0];
			$sum[] = $i[1] + $i[2] + $o[1];
			$sum[] = $i[2] + $i[3] + $o[2];
			$sum[] = $i[3] + $i[4] + $o[3];
			$sum[] = $i[4] + $i[0] + $o[4];

			$s = $sum[0];
			$ok = true;
			foreach ($sum as $t){
				if ($s!=$t){
					$ok = false;
				}
			}
			if ($ok){
				return 
					$o[0] . $i[0] . $i[1] .
					$o[1] . $i[1] . $i[2] .
					$o[2] . $i[2] . $i[3] .
					$o[3] . $i[3] . $i[4] .
					$o[4] . $i[4] . $i[0]."\n";
			}
		}
	}
	return null;
}


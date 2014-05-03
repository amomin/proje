<?php
include "pfloat.class.php";

$start=1;
$end=100;

$num_iterations = 5;
$truncate = 112;

function isSquare($x){
	$squares = array(1,4,9,16,25,36,49,64,81,100);
	if (in_array($x,$squares)){
		return true;
	}
	else return false;
}
function sq_seed($S){
	$num_digits=14;
	$x = 1/sqrt($S);
	//echo "\n";	echo $x; echo "\n";
	$d=new pfloat();
	$d->int_part=0;
	for ($i=0;$i<$num_digits;$i++){
		$x*=10;
		$int_x = intval(floor($x));
		$d->digits[]=$int_x;
		$x-=$int_x;
	}
	//echo "\n";	$d->_print(); echo "\n";
	return $d;
}

function iteration(pfloat$x, $S){
	global $truncate;
	$half = new pfloat(); $half->int_part=0; $half->digits=array(5);
	$s = new pfloat();
	$s->int_part=3; $s->digits=array();
	$x2 = $x->multiply($x);
	$w=$x2->intMult($S);
	$s->subtract($w);
	$s=$s->multiply($half);
	$new_x = $s->multiply($x);
	$new_x->truncate($truncate);
	return $new_x;
}

function digitalSum(pfloat $x){
	$sum=$x->int_part;
	for ($i=0;$i<99;$i++){
		if (isset($x->digits[$i])){
			//echo "Digit $i is {$x->digits[$i]}\n";
			$sum+=$x->digits[$i];
		}else throw new Exception("not enough digits");
	}
	return $sum;
}

$counter = 0;
$dig_sums=array();
for ($N=$start;$N<$end;$N++){
	if (! isSquare($N)){
		$y = sq_seed($N);
		for ($i=0; $i<$num_iterations; $i++){
			$y=iteration($y,$N);
		}
		$y = $y->intMult($N);
		$add = digitalSum($y); 
		$counter += $add;
		echo "digital sum for $N is $add\n";
		$y->truncate(105);
		echo "Square root of $N is about \n"; $y->_print(); echo "\n";
		$z = $y->multiply($y);
		$z->truncate(105);
		echo "Check: square is \n";$z->_print();echo "\n\n";
		$dig_sums[$N]=$add;
	}	
}
print_r($dig_sums);
echo "TOTAL COUNT IS $counter\n\n";

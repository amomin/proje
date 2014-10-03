<?php

function cont_frac($n){
	return array($n,$n);
}

function next_iterate($n){
	return 0;
}

function isSquare($n){
	$x = intval(sqrt($n));
	if ($x*$x==$n) return true;
	else return false;
}
$N=101;
for($i=0;$i<=$N;$i++){
	echo isSquare($i)?"$i is square<BR>":"no, $i is not square<BR>";
}

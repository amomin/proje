<?
include "functions.php";

$t0 = microtime(true);
$STEP = 1000;
$FROM = 500000;
$TO = 600000;

$RENORMALIZE = 10000;
for ($i=$FROM; $i<$TO; $i++){
	$f = primepowerfactorize($i);
	//$fstr=array();
	//foreach ($f as $factor){
		//$fstr[] = implode("^",$factor);
	//}
	//echo "\n$i factorized: ".implode(')*(',$fstr); 
	if ( ($i % $STEP) == 0){
		$t1 = microtime(true);
		$elapsed = $t1 - $t0;
		//$avg = $elapsed/$i;
		$avg = $RENORMALIZE*($elapsed - $prevelapsed)/$STEP;
		echo "\nTime up to $i: $elapsed s.  Average time is $avg.";
		$prevelapsed = $elapsed;
	}
}
/*
 */

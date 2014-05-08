<?php
/**
 * Just quick and dirty
 */
$num_rolls=20000; 
const DICE=6;

const GOTOJAIL= 'g2j';
const JAIL= 'jail';
const GOSTART= 'start';
const COMMUNITY_CHEST = 'cc';
const CHANCE_SQUER = 'ch';
const CH_CARDS = 16;
const CH_JAIL_CARDS = 2;

const CC_GOTOJAIL='CC_GOTOJAIL';
const CC_GOTOGO='CC_GOTOGO';
const CH_GOTOGO='CH_GOTOGO';
const CH_GOTOJAIL='CH_GOTOJAIL';
const CH_GOTOC1='CH_GOTOC1';
const CH_GOTOE3='CH_GOTOE3';
const CH_GOTOH2='CH_GOTOH2';
const CH_GOTOR1='CH_GOTOR1';
const CH_GOTONEXTR='CH_GOTONEXTR';
const CH_GOTONEXTU='CH_GOTONEXTU';
const CH_GOBACK3='CH_GOTOBACK3';

$board = array(
	GOSTART, 'a1', 'cc1', 'a2', 't1', 'r1', 'b1', 'ch1', 'b2', 'b3',
	JAIL,    'c1', 'u1' , 'c2', 'c3', 'r2', 'd1', 'cc2', 'd2', 'd3',
	'fp',    'e1', 'ch2', 'e2', 'e3', 'r3', 'f1', 'f2',  'u2', 'f3',
	GOTOJAIL,'g1', 'g2',  'cc3','g3', 'r4', 'ch3','h1',  't2', 'h2'
);

$cc_cards = array(
	'o','o','o','o', 'o','o','o','o',
	'o','o','o','o', 'o','o',CC_GOTOGO,CC_GOTOJAIL
);
$ch_cards = array(
	'o','o','o','o', 'o','o',CH_GOTOGO,CH_GOTOJAIL,
	CH_GOTOC1,CH_GOTOE3,CH_GOTOH2,CH_GOTOR1,
	CH_GOTONEXTR,CH_GOTONEXTR,CH_GOTONEXTU,CH_GOBACK3
);

shuffle($ch_cards);
shuffle($cc_cards);

$previous_doubles=array(false,false);
$numsquares= count($board);

function p84_draw(&$deck){
	$card = array_shift($deck);
	$deck[]=$card;
	return $card;
}

function move(&$loc, $n, $isDouble){
	global $previous_doubles;
	global $board;
	global $numsquares;

	//Previous Doubles, three in a row=go to jail	
	if ($isDouble){
		if ($previous_doubles[0] && $previous_doubles[1]){
			//clear doubles counter
			$previous_doubles=array(false,false);
			goToJail($loc);
			return;
		}else{
			$previous_doubles[1]=$previous_doubles[0];
			$previous_doubles[0]=true;
		}
	}else{
		$previous_doubles[1]=$previous_doubles[0];
		$previous_doubles[0]=false;
	}
	
	if ($loc + $n >= $numsquares){
		$loc = $loc+$n-$numsquares;
	}else{
		$loc = $loc+$n;
	}

	$sq = $board[$loc];

	if ($sq == GOTOJAIL){
		goToJail($loc);
	}
	if (preg_match('/^(ch|cc)/',$sq,$matches)){
		drawCard($matches[1],$loc);
	}
	return;
}

function drawCard($pile, &$loc){
	if ($pile == 'cc'){
		global $cc_cards;
		$card = p84_draw($cc_cards);
		switch($card){
			case CC_GOTOJAIL:
				goToJail($loc);
				break;
			case CC_GOTOGO:
				goToSquare($loc,GOSTART);
				break;
			default:
				break;
		}
	}else if($pile =='ch'){
		global $ch_cards;
		$card = p84_draw($ch_cards);
		switch($card){
			case CH_GOTOJAIL:
				goToJail($loc);
				break;
			case CH_GOTOGO:
				goToSquare($loc,GOSTART);
				break;
			case CH_GOTOC1:
				goToSquare($loc,'c1');
				break;
			case CH_GOTOE3:
				goToSquare($loc,'e3');
				break;
			case CH_GOTOH2:
				goToSquare($loc,'h2');
				break;
			case CH_GOTOR1:
				goToSquare($loc,'r1');
				break;
			case CH_GOTONEXTR:
				goToNextR($loc);
				break;
			case CH_GOTONEXTU:
				goToNextU($loc);
				break;
			case CH_GOBACK3:
				goBack3($loc);
				break;
			default:
				break;
		}
	}else{
		throw new Exception("No such card pile to draw from");
	}
	return $card;
}

function goToSquare(&$loc, $square){
	global $board;
	$loc = array_search($square,$board);
}
function goToNextR(&$loc){
	if ((5<$loc) && ($loc <15)){
		$loc=15;
	}
	else if ((15<$loc) && ($loc <25)){
		$loc=25;
	}
	else if ((25<$loc) && ($loc <35)){
		$loc=35;
	}
	else{
		$loc=5;
	}
}
function goToNextU(&$loc){
	if (12<$loc || $loc <28){
		$loc=28;
	}
	else{
		$loc=12;
	}
}
function goBack3(&$loc){
	global $numsquares;
	global $board;
	if ($loc > 2){
		$loc-=3;
	}else{
		$loc += $numsquares;
		$loc-=3;
	}
	$sq = $board[$loc];
	if ($sq == GOTOJAIL){
		goToJail($loc);
	}
	if (preg_match('/^(ch|cc)/',$sq,$matches)){
		drawCard($matches[1],$loc);
	}
}

function goToJail(&$loc){
	$loc=10;
}

function simulation($board, $num_rolls){
	$loc=0;
	$count=array();
	foreach ($board as $b){
			$count[$b]=0;
	}
	$move=0;
	while($move<$num_rolls){
			$move++;
			$roll1=rand(1,DICE);
			$roll2=rand(1,DICE);
			$n = $roll1 + $roll2;
			move($loc,$n, $roll1==$roll2);
			//echo "Rolled $roll1 + $roll2 = $n, now at ".$board[$loc]."\n";
			$count[$board[$loc]]+=1;
	}
	return $count;
}

$count = simulation($board, $num_rolls);
$total=array_sum($count);
arsort($count);
foreach ($count as $b=>$c){
	$percent = ($c/$total); $tp+=$percent;
	echo "Landed on $b ".sprintf("%.4f",$percent)." of the time\n";
}

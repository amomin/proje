<?php

class pfloat{
	var $digits=array();
	var $int_part;

	public function _print(){
		echo "{$this->int_part}.";
		foreach($this->digits as $d){
			echo "$d";
		}
		echo "...";
	}
	private function carry($k,$l){
		if ($k<0) {
			$this->int_part+=$l;
		}else{
			$this->digits[$k]+=$l;
			if ($this->digits[$k] > 9 ){
				$carry = intval(($this->digits[$k])/10);
				$this->digits[$k] = ($this->digits[$k] % 10);
				$this->carry($k-1,$carry);
			}
		}
	}
	public function add(pfloat $x){
		$this->int_part += $x->int_part;
		$k=0;
		$_continue = true;
		while ($_continue){
			if (isset($this->digits[$k])){
				if (isset($x->digits[$k])){
					$this->digits[$k]+=$x->digits[$k];
				}else{
					$x->digits[$k]=0;
					$this->digits[$k]+=$x->digits[$k];
				}
			}else if (isset($x->digits[$k])){
				if (!isset($this->digits[$k])) $this->digits[$k]=0;
				$this->digits[$k]+=$x->digits[$k];
			}else{
				$_continue=false;
			}
			if ($_continue && $this->digits[$k] > 9){
				$this->digits[$k]-=10;
				$this->carry($k-1,1);
			}
			$k++;
		}
	}

	public function intMult($n){
		$y=clone $this; 
		$y->int_part*=$n;
		$k=0;
		while (isset($y->digits[$k])){
				$y->digits[$k]*=$n;
				if ($y->digits[$k]>9){
					$carry = intval( ($y->digits[$k])/10);
					$y->digits[$k] = ($y->digits[$k] % 10);
					$y->carry($k-1,$carry);
				}
				$k++;
		}
		return $y;
	}
	public function _shift_left(){
		$this->int_part*=10;
		if(isset($this->digits[0])) $this->int_part+=$this->digits[0];
		$k=0;
		while(isset($this->digits[$k+1])){
			$this->digits[$k] = $this->digits[$k+1];
			$k++;
		}
		unset($this->digits[$k]);
	}
	public function _shift_right(){
		$new_digit = $this->int_part%10;
		$this->int_part = intval($this->int_part/10);
		array_unshift($this->digits,$new_digit);
	}

	public function multiply(pfloat $x){
		$y=clone $this;
		$n = $y->int_part;
		$y->int_part=0;
		$sum=$x->intMult($n);
		$k=0;
		while( isset($y->digits[0])){
			$y->_shift_left();
			$n = $y->int_part;
			$y->int_part=0;
			$term = $x->intMult($n);
			for ($i=0;$i<$k+1;$i++){
				$term->_shift_right();
			}
			$sum->add($term);
			$k++;
		}
		return $sum;	
	}
	private function neg_carry($k){
		if ($k<0) {
			$this->int_part-=1;
		}else{
			$this->digits[$k]-=1;
			if ($this->digits[$k] < 0){
				$this->digits[$k] = $this->digits[$k] +10;
				$this->neg_carry($k-1);
			}
		}
	}
	public function subtract($x){
		$this->int_part -= $x->int_part;
		$k=0;
		$_continue = true;
		while ($_continue){
			if (isset($this->digits[$k])){
				if (isset($x->digits[$k])){
					$this->digits[$k]-=$x->digits[$k];
				}else{
					$x->digits[$k]=0;
					$this->digits[$k]-=$x->digits[$k];
				}
			}else if (isset($x->digits[$k])){
				if (!isset($this->digits[$k])) $this->digits[$k]=0;
				$this->digits[$k]-=$x->digits[$k];
			}else{
				$_continue=false;
			}
			if ($_continue && $this->digits[$k] < 0){
				$this->digits[$k]+=10;
				$this->neg_carry($k-1,-1);
			}
			$k++;
		}
	
	}
	public function truncate($t){
		if (count($this->digits) > $t){
			$k=$t;
			while (isset($this->digits[$k])){
				unset($this->digits[$k]);
				$k++;
			}
		}
	}
}

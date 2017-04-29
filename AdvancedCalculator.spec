package test

import com.maths.AdvancedCalculator
import com.maths.Calculator


describe AdvancedCalculator {
	
	
	
	def table {
		| function		| value 		|
		| "x"  			| 19.7821		|
		| "x^2" 		| 82.9527		|
		| "1/x"  		| 8.41017		|
		| "1/x^2"  		| 610.655		|
		| "SQRT(x)" 	| 10.5168		|
		| "SIN(x)" 		| 0.0000232199	|
		| "COS(x)" 		| 0.00681464	|
		| "TAN(x)" 		| -20.384		|
		| "EXP(x)" 		| 538.153		|
		| "LOG(x)" 		| 5.28575		|
		| "LN(x)" 		| 5.28575		|
		| "ABS(x)" 		| 19.7821		|
		| "ASIN(x)" 	| "no result"	|
		| "ACOS(x)" 	| "no result"	|
		| "ATAN(x)" 	| "no result"	|
		| "SINH(x)" 	| 268.578		|
		| "COSH(x)"  	| 269.576		|
		| "TANH(x)" 	| 5.59686		|
		
	}
	
	def setTestCalc(String function) {
		val testCalc = new Calculator(50,50)
		testCalc.DISPLAYED_FUNCTION = function
		testCalc.setMathTree()
		return testCalc
	}
	
	describe "Testing Simpson Integral" {
		fact table.forEach[
			AdvancedCalculator.SimpsonIntegral(setTestCalc(function))
			should be value
		]
	}
	
	describe "Testing Trapezium Integral" {
		fact table.forEach[
			AdvancedCalculator.trapeziumIntegral(setTestCalc(function))
			should be value
		]
	}
	
	describe "Testing Gauss Integral" {
		fact table.forEach[
			AdvancedCalculator.gaussIntegral(setTestCalc(function))
			should be value
		]
	}


}

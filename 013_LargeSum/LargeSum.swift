/*
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Gived in LargeSum_input.txt:
  -> 100 numbers
  -> 50 digits each
*/

import Foundation

func add_numbers(str_long: String, str_short: String) -> String {

	var result = ""
	let n_long: Int = str_long.count
	let n_short: Int = str_short.count
	let n_diff = n_long - n_short
	var carry :Int = 0
	
	for i in stride(from: (n_long - 1), to: n_diff-1, by: -1) {
		//School sum
		
		let sum1 = Int(String(str_long[str_long.index(str_long.startIndex, offsetBy: i)])) ?? 0
		let sum2 = Int(String(str_short[str_short.index(str_short.startIndex, offsetBy: (i-n_diff))])) ?? 0
		let sum = sum1 + sum2 + carry

		result = String(sum%10) + result
		//Carry for next step
		//print(sum1, "+", sum2, "+", carry, "=", sum, result, sum/10)
		carry = sum / 10
	}

	//Rest of the digits of the larger number
	for i in stride(from: (n_diff - 1), to:-1, by: -1){
		let sum1 = Int(String(str_long[str_long.index(str_long.startIndex, offsetBy: i)])) ?? 0
		let sum = sum1 + carry
		result = String(sum%10) + result
		//print("n_diff")
		//print(sum1, "+", sum, " = ", result, sum/10)
		carry = sum / 10
	}

	//Add remaining carry
	if carry > 0 {
		result = String(carry) + result
		//print("Adding remaining carry")
	}
	return result
}

// main program

	let start = DispatchTime.now()
	//! Start of the program

    let filename = "LargeSum_input.txt"
    let contents = try String(contentsOfFile: filename)
    var lines = contents.split(separator:"\n")
	var sum = String(lines[0])
	//print(sum)
	for i in 1..<lines.count{
		//print(lines[i])
		sum = add_numbers(str_long:sum, str_short:String(lines[i]))
	}


print("All sum digits: ")
print(sum)

print("Last ten digits")
	for i in (sum.count - 10)..<sum.count{
		print(String(sum[sum.index(sum.startIndex, offsetBy: i)]), terminator: "")
	}
print("")

print("First ten digits")
	for i in 0...10 {
		print(String(sum[sum.index(sum.startIndex, offsetBy: i)]), terminator: "")
	}
print("")

//! End of the program
let end = DispatchTime.now()
let Time:Double = Double(end.uptimeNanoseconds - start.uptimeNanoseconds)/1_000_000
print ("\nExecuted in \(Time) ms")

/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

import Foundation

let start_time = DispatchTime.now()

func return_next_prime(previous_prime:Int) -> Int{
    
    if (previous_prime < 2){
        return 2
    }
    if (previous_prime == 2){
        return 3
    }
    var num = previous_prime
    while true{
        num = num + 2
        var prime = true
        for i in 2...(Int((Double(num)).squareRoot()+1)){
            if (num%i==0){
                prime = false
            }
        }
        if prime{
            return Int(num)
        }
    }
}


func st_prime (st_prime_number:Int)->([Int],Int){

    var prime_numbers:[Int] = [2,3]

    for _ in 3...st_prime_number{
        prime_numbers.append(return_next_prime(previous_prime: prime_numbers[prime_numbers.count-1]))
    }

    return (prime_numbers,prime_numbers[prime_numbers.count-1]) 
}

// print(return_next_prime(previous_prime: 7))
// 11
var result1 = st_prime(st_prime_number: 6) 
print(result1.0)
print(result1.1)

var result2 = st_prime(st_prime_number: 10_001) 
//print(result2.0)
print(result2.1)

let end_time = DispatchTime.now()
let msTime:Double = Double(end_time.uptimeNanoseconds - start_time.uptimeNanoseconds)/1_000_000
print ("\(msTime) ms")
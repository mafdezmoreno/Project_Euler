/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/

import Foundation

let start_time = DispatchTime.now()

func return_next_prime(previous_prime:Int) ->Int{
    if (previous_prime < 2){
        return 2
    }
    if previous_prime == 2{
        return 3
    }
    var num = previous_prime
    while (true){
        num = num + 2
        var prime = true
        for i in 2...Int(sqrt(Double(num))+1){
            if (num%i==0){
                prime = false
            }   
        }
        if (prime){
            return num
        }   
    }
}

func sum_of_primes_until(value:Int) -> Int{
    var sum = 2
    var previous_prime = 2
    while (true){
        let actual_prime = return_next_prime(previous_prime:previous_prime) 
        if (actual_prime>value){
            break
        }
        sum = sum + actual_prime
        previous_prime = actual_prime
    }
    return sum
}

print(sum_of_primes_until(value:10))
print(sum_of_primes_until(value:2000000))
let end_time = DispatchTime.now()
let msTime:Double = Double(end_time.uptimeNanoseconds - start_time.uptimeNanoseconds)/1_000_000
print ("\(msTime) ms")
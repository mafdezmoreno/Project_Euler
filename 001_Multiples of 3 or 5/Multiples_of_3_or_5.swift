//https://projecteuler.net/problem=1

/*
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 *
 */

import Foundation

let start = DispatchTime.now()

func multiples(value: Int) -> Int {
    var sum = 0
    for i in 0...value{
        if (i%3 == 0){
            sum += i
        }
        else if(i%5 == 0){
            sum += i
        }
    }
    return sum
}



let a = multiples(value: 10)
let b = multiples(value: 1000)

let end = DispatchTime.now()
let usTime:Double = Double(end.uptimeNanoseconds - start.uptimeNanoseconds)/1_000
print(a, b)
print ("\(usTime) us")
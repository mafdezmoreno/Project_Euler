/*
The sum of the squares of the first ten natural numbers is 385

The square of the sum of the first ten natural numbers is 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
*/

import Foundation

let start_time = DispatchTime.now()

func sum_squares(n:Int) -> Int{
    
    var sum = 0
    for i in 1...n{
        sum = sum + i*i
    }
    return sum
}

func square_sum(n:Int) -> Int {

    var sum = 0
    for i in 1...n{
        sum = sum + i
    }
    return sum*sum
}

func difference (last_number:Int)-> Int{
    
    return square_sum(n: last_number)-sum_squares(n: last_number)
}
//print (sum_squares(n: 10))
//print (square_sum(n: 10))
print (difference(last_number: 10))
print (difference(last_number: 100))

let end_time = DispatchTime.now()
let msTime:Double = Double(end_time.uptimeNanoseconds - start_time.uptimeNanoseconds)/1_000
print ("\(msTime) us")
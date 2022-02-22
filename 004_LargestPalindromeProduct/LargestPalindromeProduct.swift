/*
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
*/

import Foundation

let start_time = DispatchTime.now()

func digits_of_multiplication(a:Int, b:Int) -> [Int]{

    var c : Int = a*b
    var digits = [Int]()
    if (c > 99999){  
        for i in 0..<3{
            digits.insert(Int(Double(c)/pow(Double(10),Double(5-2*i))), at:i)
            c = c%Int(pow(Double(10),Double(5-2*i)))
            digits.insert(c%10,at:digits.count-i)
            c=Int(c/10)
        }
        
    }
    else{
        for i in 0..<2{
            digits.insert(Int(Double(c)/pow(Double(10),Double(4-2*i))), at:i) 
            c = c%Int(pow(Double(10),Double(4-2*i)))
            digits.insert(c%10, at: digits.count-i)
            c=Int(c/10)
        }
    }
   
    return digits
}

func equal(a:Int ,b:Int) -> Bool{
    if (a==b){
        return true
    }
    return false
}

func check_palindrome(digits:[Int]) -> Bool{
    for i in 0..<Int(digits.count/2){
        if (digits[i]==digits[digits.count-i-1]){
            continue
        }
        else{
            return false
        }
    }
    return true
}

func largest_palindrome()-> Int{
    var maximo:Int = 0
    for i:Int in (100...999).reversed(){
        for j:Int in (100...999).reversed(){
            
            let multiplication = i*j
            if (multiplication < maximo){
                break
            }
            let digits:[Int] = digits_of_multiplication(a:i,b:j)
            if (check_palindrome(digits:digits)){
                if (multiplication>maximo){
                    maximo = i*j
                }
                break
            }
        }
    }
    return maximo
}

for _ in 0..<1000{
    largest_palindrome()
}
print(largest_palindrome())
let end_time = DispatchTime.now()
let msTime:Double = Double(end_time.uptimeNanoseconds - start_time.uptimeNanoseconds)/1_000
print ("\(msTime) us")

//Debuging:

//ok print(digits_of_multiplication(a:999, b:999))
//ok print(check_palindrome(digits:[3,2,2,3]))
//ok print(check_palindrome(digits:[4,5,6,6,5,4]))
//ok print(equal(a: 1, b: 2))
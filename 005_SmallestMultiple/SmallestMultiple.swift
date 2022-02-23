import Foundation

let start_time = DispatchTime.now()

func remainder(n: Int, d:Int)-> Bool{
    if (n%d == 0){
        return true
    }
    return false
}
func check_divisible(n:Int) -> Bool{

    for i in 2...20 {
        if (remainder(n:n,d:i)){
            continue
        }
        else{
            return false
        }
    }
    return true
}

func smallest_number()-> Int{

    var i = 20
    while (true){
        //print(i, end = " ")
        if (check_divisible(n:i)){
            return i
        }
        i = i + 1
    }
}

print(smallest_number())

let end_time = DispatchTime.now()
let msTime:Double = Double(end_time.uptimeNanoseconds - start_time.uptimeNanoseconds)/1_000_000
print ("\(msTime) ms")

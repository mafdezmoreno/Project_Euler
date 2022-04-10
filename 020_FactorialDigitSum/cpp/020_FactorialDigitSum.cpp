// Source:
// https://faheel.github.io/BigInt/
/*
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
*/

#include <iostream>
#include "src/bigint.h"

int main(){
    Dodecahedron::Bigint a = 159753;
    Dodecahedron::Bigint b = 1634687496;
    
    std::cout<<(a*b)<<std::endl;
}

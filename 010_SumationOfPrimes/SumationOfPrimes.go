/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/
package main

import (
	"fmt"
	"log"
	"math"
	"time"
)

func main() {

	start := time.Now()
	//! Start of the program

	fmt.Println(sum_of_primes_until(10))
	fmt.Println(sum_of_primes_until(2_000_000))

	//! End of the program
	elapsed := time.Since(start)
	log.Printf("Time: %s", elapsed)
}

func return_next_prime(previous_prime uint) uint {

	var prime bool = true
	if previous_prime < 2 {
		return 2
	} else if previous_prime == 2 {
		return 3
	}
	num := previous_prime
	for true {
		num = num + 2
		prime = true
		var i uint
		for i = 2; i < (uint(math.Sqrt(float64(num))) + 1); i++ {
			if num%i == 0 {
				prime = false
			}
		}
		if prime {
			return num
		}
	}
	return 0
}

func sum_of_primes_until(value uint) uint {
	var sum uint = 2
	var previous_prime uint = 2
	for true {
		actual_prime := return_next_prime(previous_prime)
		if actual_prime >= value {
			break
		}
		sum = sum + actual_prime
		previous_prime = actual_prime
	}
	return sum
}

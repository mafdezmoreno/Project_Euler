/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
package main

import (
	"fmt"
	"math"
	"time"
)

func main() {
	start := time.Now()

	//number := 13195
	var number uint = 600851475143
	fmt.Println("Largest prime factor in ", number, " is: ", largest_prime_in(number))
	elapsed := time.Since(start)
	fmt.Println(elapsed)
}

func return_next_prime(previous_prime uint) uint {

	if previous_prime < 2 {
		return 2
	} else if previous_prime == 2 {
		return 3
	}
	num := previous_prime
	for true {
		num += 2
		prime := true
		for i := uint(2); i < uint(math.Sqrt(float64(num))+1); i += 2 {
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

func largest_prime_in(number uint) uint {

	var largest_prime_factor uint = 0
	var divisores uint = 1
	var i uint = 2
	for true {
		if number%i == 0 {
			divisores *= i
			largest_prime_factor = i
			if divisores >= number {
				//print(i)
				break
			}
		}
		//print(i, end= '; ')
		i = return_next_prime(i)
	}
	return largest_prime_factor
}

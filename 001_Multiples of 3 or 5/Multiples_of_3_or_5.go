//https://projecteuler.net/problem=1

// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
// Find the sum of all the multiples of 3 or 5 below 1000.

package main

import (
	"fmt"
	"log"
	"time"
)

func main() {

	start := time.Now()
	//!Start program
	a := multiples(10)
	b := multiples(1000)
	fmt.Println(a, b)
	//!End program
	elapsed := time.Since(start)
	log.Printf("Time: %s", elapsed)
}

func multiples(value int) int {
	sum := 0
	for i := 0; i < value; i++ {
		if i%3 == 0 {
			sum += i
		} else if i%5 == 0 {
			sum += i
		}
	}
	return sum
}

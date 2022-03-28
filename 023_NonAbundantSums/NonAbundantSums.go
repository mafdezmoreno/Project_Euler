/*
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
*/

/*
12 is the smallest abundant number
24 is the smallest number that can be written as the sum ot two abundant numbers
all integers greater than 28123 can be written as the sum of two abundant numbers
*/

package main

import (
	"fmt"
	"log"
	"time"
)

func main() {
	start := time.Now()
	//! Start of the program
	//test()
	///*
	var i uint
	const max = 28123 //MAX 28123

	abundant_list := get_abundant_numbers(max)
	sum_two_abundant_list := gen_sum_two_abundant(abundant_list, max)

	var sum uint = 0

	// The index give the value of the sum, and the value of array (true or false) if the number is the sum of to abundant numbers
	for i = 1; i < max; i++ {
		if sum_two_abundant_list[i] == false {
			sum += i
		}
	}

	fmt.Println("Sum of numbers writables as sum of two abundant numbers: ")
	fmt.Println(sum)

	//! End of the program
	elapsed := time.Since(start)
	log.Printf("Time: %s", elapsed)
}

func gen_sum_two_abundant(abundant_list []uint, max uint) []bool {

	two_abundant_list := make([]bool, (max + 1))
	var x int
	var y int
	for x = 0; x < len(abundant_list); x++ {
		if abundant_list[x] > max {
			break
		}
		for y = x; y < len(abundant_list); y++ {
			if abundant_list[y] > max {
				break
			}
			index := abundant_list[x] + abundant_list[y]
			if index > max {
				break
			}
			two_abundant_list[index] = true

		}
	}
	return two_abundant_list
}

func get_abundant_numbers(max uint) []uint {

	var i uint
	var abundant_list []uint
	for i = 12; i <= max; i++ {
		if check_abundant(i) {
			abundant_list = append(abundant_list, i)
			//fmt.Println(i)
		}
	}
	return abundant_list
}

func check_abundant(number uint) bool {

	abundant := false

	div := divisors(number)
	sum := array_sum(div)

	if sum > number {
		abundant = true
	}

	return abundant
}

func array_sum(arr []uint) uint {

	var sum uint = 0
	for _, item := range arr {
		sum += item
	}
	return sum
}

func divisors(number uint) []uint {

	var i uint
	var divisors []uint

	for i = 1; i <= uint(number/2); i++ {
		if number%i == 0 {
			divisors = append(divisors, i)
		}
	}
	return divisors
}

func test() {

	div := divisors(2380)
	fmt.Print(div, " ")
	sum := array_sum(div)
	fmt.Println(sum)
	fmt.Println(check_abundant(28)) //false (perfect)
	fmt.Println(check_abundant(12)) //true
	fmt.Println(check_abundant(24)) //true
	fmt.Println(check_abundant(3487))
	abundant_list := get_abundant_numbers(50)
	fmt.Println(abundant_list)
}

/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/
package main

import (
	"fmt"
	"time"
)

func main() {

	start := time.Now()
	//! Start of the program

	get_largest_sequence(1000000)

	//! End of the program
	elapsed := time.Since(start)
	fmt.Println("Time: ", elapsed)
}

func get_largest_sequence(max_value int) []int {

	var largest_seq_generator int = 0 //start number of Collatz list
	var len_Collatz int = 0
	var seq_Collatz []int

	for i := max_value; i > 0; i-- {
		temp := sequence(i)
		temp_len := len(temp)
		if temp_len > len_Collatz {
			seq_Collatz = nil
			seq_Collatz = temp
			len_Collatz = temp_len
			largest_seq_generator = i
		}
	}

	fmt.Println(largest_seq_generator)
	return seq_Collatz
}

func CollatzList_Generator() []int {
	var CollatzList []int
	for i := 1; i <= 1000000; i = i * 2 {
		CollatzList = append(CollatzList, i)
	}
	return CollatzList
}

func sequence(start int) []int {

	next := start
	sequence := []int{start}
	CollatzList := CollatzList_Generator()

	for {
		if next <= 1 {
			break
		}
		exist, index := contains_element(CollatzList, next)
		if exist {
			temp := CollatzList
			for i, j := 0, len(temp)-1; i < j; i, j = i+1, j-1 {
				temp[i], temp[j] = temp[j], temp[i]
			}
			sequence = append(sequence, temp[0:index]...)
			return sequence

		} else {
			if next%2 == 0 {
				next = if_even(next)
			} else {
				next = if_odd(next)
			}
		}

		sequence = append(sequence, next)
	}
	if next == 1 {
		return sequence
	}
	return make([]int, 0)
}

func contains_element(input []int, element int) (bool, int) {

	for i, val := range input {
		if val == element {
			return true, i
		}
	}
	return false, 0
}

func if_even(n int) int {
	return n / 2
}

func if_odd(n int) int {
	return 3*n + 1
}

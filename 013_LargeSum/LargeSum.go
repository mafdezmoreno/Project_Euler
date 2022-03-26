/*
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Gived in LargeSum_input.txt:
  -> 100 numbers
  -> 50 digits each
*/
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	"time"
)

func add_numbers(str_long string, str_short string) string {

	result := ""
	n_long := len(str_long)
	n_short := len(str_short)
	n_diff := n_long - n_short
	str_str_long := []rune(str_long)
	str_str_short := []rune(str_short)
	carry := 0

	for i := (n_long - 1); i >= (n_diff); i-- {
		//School sum
		sum1, _ := strconv.Atoi(string(str_str_long[i]))
		sum2, _ := strconv.Atoi(string(str_str_short[i-n_diff]))
		sum := sum1 + sum2 + carry

		result = strconv.Itoa(sum%10) + result
		//Carry for next step
		//fmt.Println(sum1, "+", sum2, "+", carry, "=", sum, result, sum/10)
		carry = sum / 10
	}

	//Rest of the digits of the larger number
	for i := (n_diff - 1); i >= 0; i-- {
		sum1, _ := strconv.Atoi(string(str_str_long[i]))
		sum := sum1 + carry
		result = strconv.Itoa(sum%10) + result
		carry = sum / 10
		//fmt.Println(sum1, "+", sum, " = ", result, carry)
	}

	//Add remaining carry
	if carry > 0 {
		result = strconv.Itoa(carry) + result
	}
	return result
}

func main() {

	start := time.Now()
	//! Start of the program

	file, err := ioutil.ReadFile("LargeSum_input.txt")
	sum := ""
	var lines []string

	if err != nil {
		log.Fatalf("unable to read file: %v", err)
	} else {

		//convert to array of strings
		lines = strings.Split(string(file), "\n")
		sum = lines[0]
		//fmt.Println(sum)
		for i := 1; i < len(lines); i++ {
			//fmt.Println(lines[i])
			sum = add_numbers(sum, lines[i])
		}
	}

	fmt.Println("All sum digits: ")
	//for i := 0; i < 2; i++ {
	//	fmt.Println(lines[i])
	//}
	fmt.Println(string(sum))

	fmt.Println("Last ten digits")
	for i := (len(sum) - 10); i < len(sum); i++ {
		fmt.Print(string(sum[i]))
	}

	fmt.Println("")

	fmt.Println("First ten digits")
	for i := 0; i <= 10; i++ {
		fmt.Print(string(sum[i]))
	}
	fmt.Println("")

	//! End of the program
	elapsed := time.Since(start)
	log.Printf("Time: %s", elapsed)
}

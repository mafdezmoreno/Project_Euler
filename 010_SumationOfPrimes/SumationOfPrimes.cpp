/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/

#include <iostream>
#include <math.h>       /* sqrt */
#include <chrono>
using namespace std::chrono;


int return_next_prime(int previous_prime) {
  if (previous_prime < 2) {
    return 2;
  } else if (previous_prime == 2) {
    return 3;
  }

  int num = previous_prime;

  while (true) {
    num = num + 2;
    bool prime = true;

    for (int i = 2; i <= int(sqrt(num) + 1); i++) {
      if (num % i == 0) {
        prime = false;
      }
    }
    if (prime) {
      return num;
    }
  }
}

int sum_of_primes_until(int value) {
  int sum = 2;
  int previous_prime = 2;
  while (true) {
    int actual_prime = return_next_prime(previous_prime);
    if (actual_prime > value) {
      break;
    }
    sum = sum + actual_prime;
    previous_prime = actual_prime;
  }
  return sum;
}

int main() {

  auto start = high_resolution_clock::now();

  std::cout << sum_of_primes_until(10) <<std::endl;
  std::cout << sum_of_primes_until(2000000) <<std::endl;

  auto stop = high_resolution_clock::now();
  auto duration = duration_cast<microseconds>(stop - start);
  
  std::cout << duration.count()/1000 << "ms"<< std::endl;

  return 0;
}

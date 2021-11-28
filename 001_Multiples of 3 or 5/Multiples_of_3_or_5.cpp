//https://projecteuler.net/problem=1

/*
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 *
 */
#include <iostream>
#include <chrono>
#include <vector>
using namespace std::chrono;

int multiples(int value);

int main() {
    auto start = high_resolution_clock::now();

    //! Real start of the program
    int a = multiples(10);
    int b = multiples(1000);

    std::cout<< a << std::endl;
    std::cout<< b << std::endl;

    //! Final of the program
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
  
    std::cout << duration.count() << "us"<< std::endl;
    return 0;
}

int multiples(int value) {
  int sum = 0;
  for (int i = 0; i <= value; i++) {
    if (i % 3 == 0) {
      sum += i;
    } else if (i % 5 == 0) {
      sum += i;
    }
  }
  return sum;
}

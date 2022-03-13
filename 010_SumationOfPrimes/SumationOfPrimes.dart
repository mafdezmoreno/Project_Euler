/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/

import 'dart:math';

int return_next_prime(int previous_prime) {
  if (previous_prime < 2) {
    return 2;
  } else if (previous_prime == 2) {
    return 3;
  }

  var num = previous_prime;

  while (true) {
    num = num + 2;
    var prime = true;

    for (int i = 2; i <= (sqrt(num) + 1); i++) {
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

void main() {
  final stopwatch = Stopwatch()..start();
  print(sum_of_primes_until(10));
  print(sum_of_primes_until(2000000));
  print('Executed in ${stopwatch.elapsed.inMilliseconds} ms');
}

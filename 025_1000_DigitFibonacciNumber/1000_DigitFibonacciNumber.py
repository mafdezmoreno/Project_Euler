'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

import time
from math import sqrt

def add_numbers(str_long, str_short):
  
  result = ""
  n_long = len(str_long)
  n_short = len(str_short)
  n_diff = n_long - n_short

  carry = 0
  for i in range(n_long - 1, n_diff-1, -1):
    #School sum
    sum = int(str_long[i]) + int(str_short[i - n_diff]) + carry
    result = str(sum % 10) + result
    #Carry for next step
    carry = sum // 10

  #Rest of the digits of the larger number
  
  for i in range(n_diff - 1, -1, -1):
    sum = int(str_long[i]) + carry
    result = str(sum % 10) + result
    carry = sum // 10
    #print("n_diff")
  

  #Add remaining carry
  if (carry > 0):
    result = str(carry) + result
  return result

def get_1st_term_whit_n_digits(num_digits):

    fib_seq = ["1","1"]
    index = 2
    while (len(fib_seq[-1])<num_digits):
        fib_seq.append(str(add_numbers(fib_seq[-1],fib_seq[-2])))
        index +=1
    return (fib_seq[-1], index)


def main():
    #! Start of the program
    start_time = time.time()

    print(get_1st_term_whit_n_digits(3))
    print(get_1st_term_whit_n_digits(1000))

    #! End of the program
    end_time = time.time()
    print("Execution time: %.6f ms" % ((end_time - start_time)*1000))

if __name__ == "__main__":
    main()

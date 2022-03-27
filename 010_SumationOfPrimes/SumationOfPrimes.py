'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import time
import math
start_time = time.time()

def return_next_prime(previous_prime):
    if previous_prime < 2:
        return 2
    elif previous_prime == 2:
        return 3
    num = previous_prime
    while True:
        num +=2
        prime = True
        for i in range(2,int(math.sqrt(num)+1)):
            if (num%i==0):
                prime = False
        if prime:
            return num

def sum_of_primes_until(value):
    sum = 2
    previous_prime = 2
    while (True):
        actual_prime =return_next_prime(previous_prime) 
        if (actual_prime>value):
            break
        sum = sum + actual_prime
        previous_prime = actual_prime
    return sum

print(sum_of_primes_until(10))
#print(sum_of_primes_until(2_000_000))

end_time = time.time()
print("%.6f ms" % ((end_time - start_time)*1000))
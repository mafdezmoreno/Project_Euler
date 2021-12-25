'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
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

def largest_prime_in(number):
    
    largest_prime_factor = 0
    divisores = 1
    i = 2
    while True:
        if number%i== 0:
            divisores *= i
            largest_prime_factor = i
            if (divisores>=number):
                #print(i)
                break
        #print(i, end= '; ')
        i = return_next_prime(i)
    return largest_prime_factor


#number = 13195
number = 600851475143
print("Largest prime factor in ", number, " is: ", largest_prime_in(number))
end_time = time.time()
print("%.6f us " % ((end_time - start_time)*1000000))

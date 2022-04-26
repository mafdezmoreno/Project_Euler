'''
Euler discovered the remarkable quadratic formula:
n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,
40_2 + 40 + 41 =40 (40+1)+41
 is divisible by 41, and certainly when 
n=41, 41_2+41+41
 is clearly divisible by 41.

The incredible formula 
n_2-79n+1601
 was discovered, which produces 80 primes for the consecutive values 
0 ≤ n ≤ 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n_2+an+b, where |a|<1000 and |b|≤1000
where |n| is the modulus/absolute value of n
e.g. |11|=11 and |-4|=4
Find the product of the coefficients, 
a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of 
n, starting with n=0.
'''

import math
#import cmath
import time

def return_next_prime(previous_prime):
    
    if (previous_prime < 2):
        return 2
    if (previous_prime == 2):
        return 3
    num = previous_prime
    while True:
        num = num + 2
        prime = True
        for i in range(2, int(math.sqrt(num)+1)):
            if (num%i==0):
                prime = False
        if prime:
            return num

def list_of_primes(max_value):
    actual_prime = 2
    list_to_return = [2]
    if actual_prime > max_value:
        return []
    if actual_prime == max_value:
        return list_to_return
    while True:
        temp = return_next_prime(actual_prime)
        if len(list_to_return) > max_value:
            break
        list_to_return.append(temp)
        actual_prime = temp
    return list_to_return

def solutions_quadratic_equations(b,c):
    
    #https://www.javatpoint.com/python-quadratic-equation
    a = 1
    dis_form = b * b - 4 * a * c  
    sqrt_val = math.sqrt(abs(dis_form))  
    solutions = []
  
    if dis_form > 0:  
        print(" real and different roots ")  
        sol = (-b + sqrt_val) / (2 * a)
        print(sol)  
        solutions.append(sol)
        sol = (-b - sqrt_val) / (2 * a)
        print(sol)  
        solutions.append(sol)
  
    elif dis_form == 0:  
        print(" real and same roots")  
        sol = -b / (2 * a)
        print(sol)  
        solutions.append(sol)
    
    else:  
        print("Complex Roots") 
        print(- b / (2 * a), " + i", sqrt_val)  
        print(- b / (2 * a), " - i", sqrt_val)   
    
    return solutions

def check_values(max):

    primes_values = list_of_primes(max)
    counter_max = 0
    prime_values_by_formula = []
    a_b = 0
    for a in range (-999,1000,2):
        for b in range (1, 1001,2):
            prime_counter = 0
            temp_prime_values_by_formula = []
            for n in range (0,79):
                value = n*n+a*n+b
                if value in primes_values:
                    counting = True
                    temp_prime_values_by_formula.append(value)
                    prime_counter+=1
                    if prime_counter > counter_max:
                        counter_max = prime_counter
                        prime_values_by_formula = temp_prime_values_by_formula
                        a_b = a*b
                        print(n, a, b, value, prime_counter)
                else:
                    break
    print(prime_values_by_formula)
    print(counter_max)
    print(a_b)
    #print(primes_values)

def test():
    '''
    print(list_of_primes(20))
    print(list_of_primes(2))
    print(list_of_primes(1))
    print(solutions_quadratic_equations(5,6))
    print(solutions_quadratic_equations(2,3))
    '''
    check_values(10000)


def main():
    
    #! Start of the program
    start_time = time.time()
    #test()
    check_values(10000)
    #! End of the program
    end_time = time.time()
    print("Execution time: %.3f s" % ((end_time - start_time)))


if __name__ == "__main__":
    main()
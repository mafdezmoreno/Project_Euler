#https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import time

start_time = time.time()

def multiples(value):
    sum = 0
    for i in range(value):
        if i%3 == 0:
            #print (i, end=' ')
            sum += i
        elif i%5 == 0:
            #print (i, end=' ')
            sum += i
    return sum



a = multiples(10)
b = multiples(1000)
stop_time = time.time()
print(a, b)
print("%.3f ms" % ((stop_time - start_time)*1000))
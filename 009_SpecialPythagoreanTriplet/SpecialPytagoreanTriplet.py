'''


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
aˆ2 + bˆ2 = cˆ2

For example, 3ˆ2 + 4ˆ2 = 9 + 16 = 25 = 5ˆ2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

https://en.wikipedia.org/wiki/Pythagorean_triple

Euclid's is a fundamental formula for generating Pythagorean triples given an arbitrary pair of integers m and n with m > n > 0. The formula states that the integers

    a = mˆ2 − nˆ2 ,   
    b = 2*m*n ,  
    c = mˆ2 + nˆ2
'''

'''
a+b+c = 1000

c = 1000 - a - b

1000 -a -b = mˆ2 -nˆ2

1000 -mˆ2 + nˆ2 -b = mˆ2 +n ˆ2

1000 -2mˆ2 = 2*m*n

2mˆ2 + 2mn -1000 = 0 //quadratic equation

'''

import math

def solution(a, b, c, n):
    # https://www.programiz.com/python-programming/examples/quadratic-roots
    # calculate the discriminant
    b = b*n
    d = (b**2) - (4*a*c)
    # find two solutions
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)

    #print('The solution are {0} and {1}'.format(sol1,sol2)) 
    m = sol2
    a = m*m - n*n
    b = 2*m*n
    c = m*m + n*n
    if ((a>0)and(b>0)):
        if ((a%1==0)and(b%1==0)):
            print(a, b, c)
            print (a+b+c)
            print (a*b*c)
            print()
    m = sol1
    a = m*m - n*n
    b = 2*m*n
    c = m*m + n*n
    if ((a>0)and(b>0)):
        if ((a%1==0)and(b%1==0)): 
            print(a, b, c)
            print (a+b+c)
            print (a*b*c)
            print()


# 2mˆ2 + 2mn -1000 = 0
# n = 1
#solution (2, 2, -1000, 1)
# n = 2
#solution (2, 2, -1000, 2)

def list_solutions():
    for i in range(100):
        solution(2,2,-1000,i)

list_solutions()
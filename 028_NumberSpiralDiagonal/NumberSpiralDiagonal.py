
'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
 43
 42 21 22 23 24 25 26
 41 20  7  8  9 10 27
 40 19  6  1  2 11 28
 39 18  5  4  3 12 29
 38 17 16 15 14 13 30
 37 36 35 34 33 32 31
It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

import time
start_time = time.time()
diagonal=2
d = 1
sum = 1
max_diagonal_size = 1001
for _ in range (0, max_diagonal_size//2):
    print("diagonal", diagonal+1)
    for _ in range(0,4):
        d=d+diagonal
        print(d, end = " ")  
        sum = sum + d
    print()
    diagonal = diagonal+2
print (sum)

stop_time = time.time()
print("Executed in %.3f ms" % ((stop_time - start_time)*1000))
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
import time
start_time = time.time()

def remainder(n,d):
    if n%d == 0:
        return True
    return False

def check_divisible(n):

    for i in range(2,20):
        if remainder(n,i):
            continue
        else:
            return False
    return True


def smallest_number():

    i = 20
    while True:
        
        #print(i, end = " ")
        if check_divisible(i):
            return i
        i = i + 1

#print(remainder (20, 5))
#print(check_divisible(100))
print(smallest_number())

end_time = time.time()
print("%.6f ms" % ((end_time - start_time)*1000))
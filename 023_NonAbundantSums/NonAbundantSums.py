#Source:
# https://stackoverflow.com/questions/45638830/project-euler-23-python-non-abundant-sums

import math

def getDivisors(num):
    if num==1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while (divisor < n):
        if (num%divisor == 0):
            total += divisor
            total += num//divisor
        divisor+=1
    if n**2==num:
        total+=n
    return total

def isAbundant(num):
    if (getDivisors(num) > num):
        return True
    else:
        return False



#! Start of the program
import time
from math import sqrt
start_time = time.time()

max = 28124

abundentNums = []
for x in range (0,max):
    if (isAbundant(x)):
        abundentNums.append(x)
        #print(x)
del abundentNums[0]

sums = [0]*28124
for x in range (0, len(abundentNums)):
    for y in range (x, len(abundentNums)):
            sumOf2AbundantNums = abundentNums[x]+abundentNums[y]
            if (sumOf2AbundantNums<= 28123):
                if (sums[sumOf2AbundantNums] == 0):
                    sums[sumOf2AbundantNums] = sumOf2AbundantNums
#print(sums)
total = 0
for x in range (1,len(sums)):
    if (sums[x] == 0):
        #print(x)
        total +=x

print("Sum of numbers writables as sum of two abundant number: ")
print(total)

#! End of the program
end_time = time.time()
print("%.6f ms" % ((end_time - start_time)*1000))
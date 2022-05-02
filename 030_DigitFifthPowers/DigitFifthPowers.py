'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1ˆ4 + 6ˆ4 + 3ˆ4 + 4ˆ4
8208 = 8ˆ4 + 2ˆ4 + 0ˆ4 + 8ˆ4
9474 = 9ˆ4 + 4ˆ4 + 7ˆ4 + 4ˆ4
As 1 = 1ˆ4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import time
start_time = time.time()

power = 5
max = power*9**power
print("max", max)

def power_digit(value, power):
    temp = str(value)
    digits = []
    sum = 0
    for digit in temp:
        digits.append(int(digit))
        sum = sum + int(digit)**power
    #print(digits, sum)
    return sum
def sum_array(arr):
    sum = 0
    for item in arr:
        sum+= item
    return sum

powers_of_their_digits = []
for i in range(2,int(max)+1):
    if i == power_digit(i, power):
        powers_of_their_digits.append(i)
        print(i)
print(powers_of_their_digits)
print(sum_array(powers_of_their_digits))

stop_time = time.time()
print("Executed in %.3f ms" % ((stop_time - start_time)*1000))
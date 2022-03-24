'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

Gived in LargeSum_input.txt:
  -> 100 numbers
  -> 50 digits each
'''

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

  #Add remaining carry
  if (carry > 0):
    result = str(carry) + result
  return result


#! Start of the program
import time
from math import sqrt
start_time = time.time()


#file = open('013_LargeSum/LargeSum_input.txt', 'r')
file = open('LargeSum_input.txt', 'r')
sum = ''

if file:
    
    #Read file
    lines = file.readlines()
    #print(lines)

    sum = lines[0][:-1]
    #print(sum)
    for i in range(1, len(lines)):
      sum = add_numbers(sum, lines[i][:-1])
      #print(lines[i])

else:
    print("File not found")


#test_add = add_numbers('2345', '567');
#print(test_add);

print("All sum digits: ")
print(sum)

print("Last ten digits")
for i in range(len(sum) - 10, len(sum)):
  print(sum[i], end="")

print('')

print("First ten digits")
for i in range (0, 10):
    print(sum[i], end='')

print('')

#! End of the program
end_time = time.time()
print("%.6f ms" % ((end_time - start_time)*1000))
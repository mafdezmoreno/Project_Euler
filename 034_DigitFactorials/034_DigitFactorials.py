'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

'''

def factorial(n):
    
    f = 1
    if n == 0:
        return 1
    for i in range(1,n+1):
        f = f * i
    return f

facts = list()

for i in range(0, 10):
    facts.append(factorial(i))

print(facts)

def sum_dig_fac(n):

    nstr = str(n)
    sum = 0
    for i in nstr:
        sum = sum + facts[int(i)] # factorial(int(i))
    return sum
    
## Tests
# print(sum_dig_fac(145))
# print(factorial(14)) # 87178291200

sum = 0
for i in range (3, 22540161):
    temp = sum_dig_fac(i)
    #print (temp)
    if i == temp:
        print ("OK", i)
        sum = sum + i
print(sum)

# Answer:  40730

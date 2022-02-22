'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
import time
start_time = time.time()

def digits_of_multiplication(a, b):

    c = a*b
    #print (c)
    digits = []
    if c>99999:      
        for i in range(3):
            digits.insert(i, int(c/(10**(5-2*i)))) 
            c = c%(10**(5-2*i))
            digits.insert(len(digits)-i,c%10)
            c=int(c/10)
        #print(digits)

    else:
        for i in range(2):
            digits.insert(i, int(c/(10**(4-2*i)))) 
            c = c%(10**(4-2*i))
            digits.insert(len(digits)-i,c%10)
            c=int(c/10)
        #print(digits)
    return digits

def equal(a ,b):
    if a==b:
        return True
    return False

def check_palindrome(digits):
    for i in range(int(len(digits)/2)):
        if digits[i]==digits[len(digits)-i-1]:
            #print(digits[i], digits[len(digits)-i-1])
            continue
        else:
            return False
    return True

def largest_palindrome():
    palindromes = []
    maximo = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            multiplication = i*j
            if multiplication < maximo:
                break
            digits = digits_of_multiplication(i,j)
            #print (i,j, i*j, digits)
            if (check_palindrome(digits)):
                #palindromes.append(i*j)
                if (i*j)>maximo:
                    maximo = i*j
                break
    return maximo

# Debug code:
#digits_of_multiplication(999, 999)
#digits_of_multiplication(123, 123)
#print(check_palindrome([3,2,2,3]))
#print(check_palindrome([3,2,0,3]))
#print(check_palindrome([4,5,6,6,5,4]))


for i in range(1000):
    largest_palindrome()

print(largest_palindrome())

end_time = time.time()
print("%.6f us" % ((end_time - start_time)*1000000))

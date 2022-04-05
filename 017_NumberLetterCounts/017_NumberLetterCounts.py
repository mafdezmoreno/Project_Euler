'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

import re


def number_to_word(number, index):

    if index == -1:
        word = ["ten", "eleven", "twelve", "thirteen" , "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        return " " + word[number]
    if number == 0:
        return ""
    if index == 0 or index == 2 or index == 3:
        word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        if index == 2:
            return " "+ word[number-1] + " hundred"
        elif index == 3:
            return word[number-1] + " thousand"
        return " "+ word[number-1]
    if index == 1:
        word = ["twenty" , "thirty", "forty", "fifty" , "sixty", "seventy", "eighty", "ninety"]
        return " " + word[number-2]
   

   

def number_to_digits(number):

    digits = []
    while number>9:
        digits.insert(0,number%10)
        number = number//10
    digits.insert(0, number)
    return digits

def write_number(number):

    writing = ""
    digits = number_to_digits(number)
    i = len(digits) - 1 
    for element in digits:
        if element < 2 and element > 0 and i == 1:
            writing = writing + number_to_word(digits[-1], -1)
            break
        writing = writing + number_to_word(element, i)
        if i == 2 and element != 0 and (digits[-2] != 0 or digits[-1] !=0):
            writing = writing + " and"
        i -=1
    return writing



# Testing funcions

'''
# number_to_word Test 1
for i in range(1,10):
    print(number_to_word(i,0))

# number_to_digit
print(number_to_digits(123))

# write_number

print(800)
print(write_number(800))
print(810)
print(write_number(810))

print(110)
print(write_number(110))
print(10)
print(write_number(10))
print(12)
print(write_number(12))

print(1234)
print(write_number(1234))

print(1230)
print(write_number(1230))

print(1200)
print(write_number(1200))

print(1000)
print(write_number(1000))
'''

# General Tests
'''
counter = 0
for i in range (0, 6):

    temp = write_number(i)
    temp_counter = 0
    for element in temp.split(" "):
        temp_counter = temp_counter + len(element)
    counter = counter + temp_counter
    print(i, ": ", temp, "==>>", counter)

counter = 0
for i in range (342, 343):

    temp = write_number(i)
    temp_counter = 0
    for element in temp.split(" "):
        temp_counter = temp_counter + len(element)
    counter = counter + temp_counter
    print(i, ": ", temp, "==>>", counter)

counter = 0
for i in range (115, 116):

    temp = write_number(i)
    temp_counter = 0
    for element in temp.split(" "):
        temp_counter = temp_counter + len(element)
    counter = counter + temp_counter
    print(i, ": ", temp, "==>>", counter)
'''

#Final Check
#'''
counter = 0
for i in range (0, 1001):

    temp = write_number(i)
    temp_counter = 0
    for element in temp.split(" "):
        temp_counter = temp_counter + len(element)
    counter = counter + temp_counter
    print(i, ": ", temp, "==>>", counter)
#'''
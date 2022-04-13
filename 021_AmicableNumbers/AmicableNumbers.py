'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
def divisor_sum_list(until_number):
    divisor_sum_list = {}
    for i in range(1, until_number+1):
        divisor_sum_list[i] = sum_array(divisors(i))
    return divisor_sum_list

def look_for_amicables(input_dict):
    
    amicable_item = []
    for element_a in input_dict:
        if element_a in amicable_item:
            continue
        element_b = input_dict[element_a]
        if element_b in input_dict:
            if element_a != element_b:
                if input_dict[element_b] == element_a:
                    amicable_item.append(element_a)
                    amicable_item.append(element_b)
                    #print(element_a, element_b)
    return amicable_item

def print_dictionary(input):

    for element in input:
        print (element, input[element])

def divisors(number):
    divisors = []
    for i in range(1,(number//2+1)):
        if number%i == 0:
            divisors.append(i)
    return divisors

def sum_array(input):
    sum = 0
    for element in input:
        sum += element
    return sum

def tests():
    test1 = divisors(220)
    print(test1) 
    print(sum_array(test1))
    print_dictionary(divisor_sum_list(100))
    amicables = look_for_amicables(divisor_sum_list(10000))
    print(amicables)
    print(sum(amicables))

def solution():
    amicables = look_for_amicables(divisor_sum_list(10000))
    #print(amicables)
    print(sum(amicables))

#tests()
solution()
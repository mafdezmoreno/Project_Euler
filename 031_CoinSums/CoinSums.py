'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

# Solution based on:
# https://www.educative.io/edpresso/coin-change-problem-2-finding-the-number-of-ways-to-make-a-sum

import time
start_time = time.time()

def find_possible_ways(coins, sum):
    
    size = len(coins)

    # Declaring a 2-D array
    # for storing solutions to subproblems:
    arr = [[0] * (sum + 1) for x in range(size + 1)]

    # Initializing first column of array to 1
    # because a sum of 0 can be made
    # in one possible way: {0}
    for i in range(size + 1):
        arr[i][0] = 1

    #Solution
    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            if coins[i - 1] > j:  # Cannot pick the highest coin:
                arr[i][j] = arr[i - 1][j]
            else:  # Pick the highest coin:
                arr[i][j] = arr[i - 1][j] + arr[i][j - coins[i - 1]]

    return arr[size][sum]


coins = [2 ,1]  # Array of available coins
sum = 5  # The sum to be made

print("The possible ways %s can be made is %s" % (sum, find_possible_ways(coins, sum)))

coins = [200, 100, 50, 20, 10 , 5, 2 ,1]  # Array of available coins
sum = 200  # The sum to be made

print("The possible ways %s can be made is %s" % (sum, find_possible_ways(coins, sum)))

stop_time = time.time()
print("Executed in %.3f us" % ((stop_time - start_time)*1000000))
'''
Consider all integer combinations of aˆb for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

2ˆ2=4, 2ˆ3=8, 2ˆ4=16, 2ˆ5=32
3ˆ2=9, 3ˆ3=27, 3ˆ4=81, 3ˆ5=243
4ˆ2=16, 4ˆ3=64, 4ˆ4=256, 4ˆ5=1024
5ˆ2=25, 5ˆ3=125, 5ˆ4=625, 5ˆ5=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
'''

import time
start_time = time.time()

max_value = 100
values = []
for i in range(2,max_value+1):
    values.append(i)
sequence = []
for base in values:
    for exp in values:
        value = base**exp
        #value = [base, exp]
        print(value, end=" ")
        if value in sequence:
            continue
        else:
            sequence.append(value)
    print()
print("Number of distinct terms: ", len(sequence))

stop_time = time.time()
print("Executed in %.3f ms" % ((stop_time - start_time)*1000))
#!/usr/bin/env  python3
#source Learn Python The Hard way

def add_numbers(max, step=1):
    i = 0
    numbers = []
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

numbers = add_numbers(10, 2)

print "The numbers: "

for num in numbers:
    print num


# Results

#  At the top i is 0
#  Numbers now:  [0]
#  At the bottom i is 2
#  At the top i is 2
#  Numbers now:  [0, 2]
#  At the bottom i is 4
#  At the top i is 4
#  Numbers now:  [0, 2, 4]
#  At the bottom i is 6
#  At the top i is 6
#  Numbers now:  [0, 2, 4, 6]
#  At the bottom i is 8
#  At the top i is 8
#  Numbers now:  [0, 2, 4, 6, 8]
#  At the bottom i is 10
#  The numbers:
#  0
#  2
#  4
#  6
#  8

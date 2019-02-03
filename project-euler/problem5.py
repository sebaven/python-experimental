"""
2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

smallest_value = 0
value = 0
while smallest_value == 0:
    value = value + 1
    for i in range(1, 20):
        if value % i != 0:
            break
    else:
        smallest_value = value

print("the smallest positive number that is evenly divisible by all of the numbers from 1 to 20: %s" % smallest_value)

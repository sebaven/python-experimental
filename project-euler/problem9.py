"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math


def find_pythagorean_triplet():
    depth = 1000
    for x in range(1, depth):
        for y in range(x + 1, depth):
            for z in range(y + 1, depth):
                s1 = x + y + z
                s2 = math.pow(x, 2) + math.pow(y, 2)
                s3 = math.pow(z, 2)
                if s1 == 1000 and s2 == s3:
                    return x * y * z


print("The product of Pythagorean triplet for which a + b + c = 1000: %s" % find_pythagorean_triplet())

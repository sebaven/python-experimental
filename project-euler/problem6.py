"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""
import math

sum_of_squares = 0
for i in range(1, 101):
    sum_of_squares = sum_of_squares + math.pow(i, 2)

s = 0
for i in range(1, 101):
    s = s + i

square_of_sum = math.pow(s, 2)
difference = square_of_sum - sum_of_squares

print(
    "difference between the sum of the squares of the first" +
    "one hundred natural numbers and the square of the sum: %s" % difference)

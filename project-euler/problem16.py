"""

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

number = 2**1000
string = str(number)
sum = 0
for c in string:
    sum = sum + int(c)

print("the sum of the digits of the number 2e1000: %s" % sum)

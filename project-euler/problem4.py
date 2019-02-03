"""
A palindromic number reads the same both ways.
he largest palindrome made from the product of

Find the largest palindrome made from the product of two 3-digit number
"""

largest_palindrom = 0
for a in range(100, 999):
    for b in range(100, 999):
        value = a * b
        s1 = str(value)
        s2 = s1[::-1]
        if s1 == s2 and value > largest_palindrom:
            largest_palindrom = value

print("Largest palindrom from the product of to 3-digits numbers: %s" %
      largest_palindrom)

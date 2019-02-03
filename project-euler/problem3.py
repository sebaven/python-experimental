"""

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def get_largest_prime_factor(number):
    n = number
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n = n // d
        d += 1
    if n > 1:
        factors.append(n)
    return max(factors)


largest_factor = get_largest_prime_factor(600851475143)
print("Largest prime factor of the number 600851475143: %s" % largest_factor)

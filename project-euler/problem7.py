"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def nth_prime(rank):
    prime_found = 0
    count = 0
    while prime_found != rank:
        count = count + 1
        if is_prime(count):
            prime_found = prime_found + 1
    else:
        return count


prime = nth_prime(10001)
print("the 10 001st prime number: %s" % prime)

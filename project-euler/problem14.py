"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""


def is_even(n):
    return n % 2 == 0


def compute_even(n):
    return n / 2


def compute_odd(n):
    return (3 * n) + 1


def compute(n):
    if is_even(n):
        return compute_even(n)
    else:
        return compute_odd(n)


def count_chain(n):
    value = n
    count = 0
    while value != 1:
        value = compute(value)
        count = count + 1
    return count


longest_chain = 0
candidate = 0
start = 1
end = 1_000_000
for i in range(start, end):
    chain_count = count_chain(i)
    if chain_count > longest_chain:
        longest_chain = chain_count
        candidate = i

print("longest chain number: %s" % candidate)

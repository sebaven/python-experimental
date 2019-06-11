"""

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def get_proper_divisors(val):
    d = []
    for i in range (1,val):
        if val % i == 0:
            d.append(i)
    return d

def d(val):
    divisors = get_proper_divisors(val)
    return sum(divisors)

def is_amicable(a):
    b = d(a)
    value = d(b)
    return b != value and value == a


limit = 10_000
amicable_numbers = []

for i in range(1,limit):
 if is_amicable(i):
     amicable_numbers.append(i)
     
sum = sum(amicable_numbers)

print("the sum of all the amicable numbers under %s: %s" % (limit,sum))

  
    
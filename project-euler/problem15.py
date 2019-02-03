"""
lattice paths
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""

""" 
Never heard of Lattice paths before
some study was needed but a good introduction on the formula is described here:
https://www.robertdickau.com/manhattan.html
paths = (2n)!/(n!^2)
"""

n = 20

a = 1
for i in range(1, (2 * n) +1):
    a = a * i

b = 1
for j in range(1, n+1):
    b = b * j

paths = a / (b * b)
print ("Amount of paths through a 20x20 grid: %s" % paths)


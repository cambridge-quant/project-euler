"""
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""

from math import comb

dimension = 20

answer = comb(2*dimension, dimension)
print(answer)
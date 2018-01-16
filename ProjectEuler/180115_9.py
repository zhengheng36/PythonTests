
# Special Pythagorean triplet
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.



# It: 利用数学方法，首先做了一个因式分解，简化问题
b = 1
for a in range(200, 1000000):
    b = 1
    while True:
        if b == a:
            break
        b = b + 1
        k = 1000*(a + b) - a * b
        if k == 500000:
            break
    if k == 500000:
        break

        
print('a:', a)
print('b:', b)

# KEY: in order to use 'square'
from math import sqrt
c = sqrt(a * a + b * b)
print('c:', int(c))


# understand two ways of deving

a = 10
b = 3

c = a / b
print('c is:', c)

d = a // b
print('d is:', d)   # // can always end up with int

a = 10.998
d = a // b
print('d is:', d)   # // can always end up with int, not matter what will be after '.' will be discraded.

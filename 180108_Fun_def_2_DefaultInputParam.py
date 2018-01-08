# def: default input parameter

## basic
def my_power(x, n=2):
    result = 1
    while n != 0:
        result = result * x
        n = n - 1
    
    return result

print('2^2 is:',my_power(2))    # KEY: without second input parameter, the default value of 2 will apply
print('2^3 is:',my_power(2, 3))
print('3^3 is:',my_power(3, 3))
print()

## advance
# example1
def my_add_end(L=[]):
    L.append('END')
    return L

cnt = 3
while cnt != 0:
    print(my_add_end()) 
    # the result is interesting because, it add 'END' based on last call, which should not be
    # It: the reason is because, when fisrt call this function, the L has been created. As label 
    cnt = cnt - 1
print()

# example2
def my_add_end_2(L=None):
    if L is None:
        L = []      # fixed it by reset value of L everytime
    L.append('END')
    return L

cnt2 = 3
while cnt2 != 0:
    print(my_add_end_2()) 
    cnt2 = cnt2 - 1
print()



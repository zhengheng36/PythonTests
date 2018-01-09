## sort can be used as higher-order function


## basic sort: 
# KEY: the input parameter should be only one, which is list
print(sorted([2, 7, 8, 12, 5, 3, 0, 4]))
print()

## used as higher-order function
# KEY: the input parameter should be two, first is list, the other is functionName
def sortKey1(ch):
    return ch.lower()

def sortKey2(x):
    return abs(x)

print(sorted(['v', 't', 'a', 'e', 'b'], key = sortKey1))
print()
print(sorted([-100, 102, 111, -106], key = sortKey2))
print()

## practice
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)] # Tuple is define by '()', List is by '[]'

def by_name(t): # KEY: consider evey t is: ('XXX', YYY), so that it can be visied by t[0] and t[1]
    return t[0]

def by_score(t):
    return t[1]

print('The type of L is:', type(L))
print('The type of elements in L is:', type(L[0]))
print()
print(sorted(L, key = by_name))
print(sorted(L, key = by_score))

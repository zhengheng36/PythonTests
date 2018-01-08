# quick way of generating a new list for existing list

ListOriginal = [1, 2, 3, 4, 5, 6, 7]

## original way
print('Original way of doing:')
def NewList1(ListOri):
    L = []
    for num in ListOri:
        L.append(num * 10)
    
    return L

print(NewList1(ListOriginal))
print()

## advanced way
# Example1:
print('Advance way of doing number:')
NewList2 = [num2*10 for num2 in ListOriginal] # format: [items in new list for xx in YYY]
print(NewList2)
print()


# Example2:
print('Advance way of doing char:')
ListChOri = ['A', 'b', 'C', 'd']
ListNewCh = [ch.lower() for ch in ListChOri]
print(ListNewCh)
ListNewCh = [ch.upper() for ch in ListChOri]
print(ListNewCh)
print()

# Example3:
print('Advance way of doing combined with range:')
ListNumPow = [num3 * num3 for num3 in range(1, 10)]
print(ListNumPow)
print()

# Example4:
print('Advance way of doing two loops:')
ListChars = [ch1 + ch2 for ch1 in 'ABCD' for ch2 in '1234']
print(ListChars)
print()

# Example5:
print('Advance way of doing dictionary:')
d = {'A': '1', 'B': '2', 'C': '4'}
ListDictItem = [k + '=' + v for k, v in d.items()]
print(ListDictItem)


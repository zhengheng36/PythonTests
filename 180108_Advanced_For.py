## advance of using for

## for for dic
dictInput = {'A': 65, 'B': 66, 'C': 67} # define

print("\nKeys:")
for key in dictInput:
    print(key)

print("\nValues:")
for value in dictInput.values():
    print(value)

print("\nKey-Value")
for key, value in dictInput.items():
    print(key, ' = ', value)


## for for char
print('\nchr')
for ch in 'ABCDefG':
    print(ch)

## for for index
print('\nprint with index')
for i, value in enumerate(['A', 'b', 'C', 'd']):
    print(i, value)

## for for list
print()
for x, y in [(1, 1), (2, 2), (3, 3), (4, 4)]:
    print('x=',x,', y=',y)

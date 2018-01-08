## use slice to handle list

## define
def printListNumSlice(listNum):
    print('listNum', listNum)

    ## examples
    print('listNum[0:10]', listNum[0:10])        # euqal
    print('listNum[:]', listNum[:])           # equal

    print('listNum[0:5]', listNum[0:5])
    print('listNum[1:5]', listNum[1:5])

    print('listNum[0:8]', listNum[0:8])
    print('listNum[:8]', listNum[:8])          # euqal

    print('listNum[0:10:2]', listNum[0:10:2])  
    print('listNum[:10:2]', listNum[:10:2])       # equal
    print('listNum[::2]', listNum[::2])         # euqal

    print('listNum[::5]', listNum[::5])         # every 5 elements


print("Example1: numbers")
listNum1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
printListNumSlice(listNum1)

print()

## same idea for str
print("Example2: strings")
listNum2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
printListNumSlice(listNum2)


## List basic examples and Tuple 

## List
# Define List
listTest = ['1', 2, '3', '4']

# Check number inside List
print('The elements inside the listTest is:', len(listTest))

# Visit List
print('They are:', listTest)
print('The first element is:', type(listTest[0]), listTest[0])
print('The second element is:', type(listTest[1]), listTest[1])
print('The last element is:', listTest[-1])
print('The second last element is:', listTest[-2])

# Add elements into List
listTest.append('E')
print('After append:', listTest)
listTest.insert(0, 'ZERO')
print('After insert:', listTest)

# Delete element from List: index begin with 0
listTest.pop()
print('After pop():', listTest)
listTest.pop(0)
print('After pop(0):', listTest)

# Add List into List
listTest2 = [listTest, 'F', 'G']
print('The first list is:', listTest)
print('The second list is:', listTest2)
print('The the first element of first list from second list varable name', listTest2[0][0]) # look like 2D array

## The unchangeable List is Tuple. 
# Tuple can be visited
tupleTest = ('A', 'B', 'C') # it is () instead of []
print('The number inside this tuple is:', len(tupleTest))
print('First element in this tuple is:', tupleTest[0])
print('Last element in this tuple is:', tupleTest[-1])

# 1 element Tuple should be defined in this way
tupleOneElement = (1, )
print('tupleOneElement is', tupleOneElement)

# Element's elements inside Tuple can be changed
listInTuple = ['A', 'B']
tupleWithList = (1, '2', listInTuple)
print('tupleWithList is', tupleWithList)

tupleWithList[2][0] = 'C'   # Key, we cannot change elements of tuple, but we can change tuple's elements' element
tupleWithList[2][1] = 'D'
print('After changing tupleWithList is', tupleWithList)

## sort and replace str in list
listTest3 = ['b', 'c', 'd', 'a']
print('listTest3 before sort():', listTest3)
listTest3.sort() # not return value, the sort method apply to listTest3 elements
print('listTest3 after sort():', listTest3) # check listTest3 to see result

stringA = 'ABC'
print('stringA before replace():', stringA)
stringA.replace('A', 'a')
print('stringA after replace():', stringA)

stringB = stringA.replace('A', 'a') # think in labeling way
print('stringB after replace():', stringB)






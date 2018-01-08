## Dictionary and Set

## dic: key-value pair. key cannot be changed
# define
dictionaryTest = {'A': 65, 'B': 66, 'C': 67}
print()

# print
print('dictionaryTest is:', dictionaryTest)
print()

# get value
print('dictionaryTest key A value is:', dictionaryTest['A'])    # value = dictionaryTest['key']
print('dictionaryTest key B value is:', dictionaryTest['B'])
print('dictionaryTest key C value is:', dictionaryTest['C'])
print()

# try to get value
tryToGet = dictionaryTest.get('E')
print('get() is trying to get the value of a key, if not found, return NONE:', tryToGet)
tryToGet = dictionaryTest.get('E', -1)
print('get() is trying to get the value of a key, if not found, output second parameter:', tryToGet)
print()

# change value
dictionaryTest['C'] = 99
print('dictionaryTest key C value after changing is:', dictionaryTest['C'])
print()

# add key
dictionaryTest['E'] = 100 # !!!!!the way of adding is special
print('dictionaryTest after adding/assigin is:', dictionaryTest)
print()

# check key
if 'E' in dictionaryTest:
    print('E is found in dictionaryTest')
else:
    print('E is NOT found in dictionaryTest')
print()

# remove key
print('dictionaryTest before pop(key) is:', dictionaryTest)
dictionaryTest.pop('C')
print('dictionaryTest after pop(key) is:', dictionaryTest) # there is not pop(), must with key
print()

## set: dictionary without values. keys/elements in set cannot be the same
# define
setTest1 = set([1, 2, 3, 4, 56])
print('The set1 is:', setTest1)
print()

# add
setTest1.add(8)
print('The set1 after adding is:', setTest1)
print()

# remove
setTest1.remove(56)
print('The set1 after removing is:', setTest1)
print()

# op
setTest2 = set([3, 4, 5, 6, 7, 8])
print('The set1 is:', setTest1)
print('The set2 is:', setTest2)

print('setTest1 | setTest2 is:', setTest1 | setTest2)
print('setTest1 & setTest2 is:', setTest1 & setTest2)
print('setTest2 & setTest1 is:', setTest2 & setTest1)
print()

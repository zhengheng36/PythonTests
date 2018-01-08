## Generator( different from List)
ListExample = [x*x for x in range(1, 10)]
print('ListExample:', ListExample)

# define
GenerateExample = (x*x for x in range(1, 10))   # compared with list, the outside blacket is different
print('GenerateExample:', GenerateExample)

# Get next
print('next:')
# print(next(GenerateExample))
# print(next(GenerateExample))
# print(next(GenerateExample))
print() # when enable, we can find that the next number is next one, even if we use for insetead of next()

# iterate: msot of time, we will use for instead of next
print('Iterate:')
for n in GenerateExample:
    print(n)
print()

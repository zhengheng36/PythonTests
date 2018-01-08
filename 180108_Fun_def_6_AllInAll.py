# combined of all kinds of def call

def my_all(a, *b, **c):
    print(a)
    print(b)
    print(c)
    

b = [1, 2, 3, 4, 5, 6]
c = {'A': 100, 'Z': 200, 'C': 300}

my_all(678, *b, **c)
## return value can be a function name


## basic

def myFunc1(x):
    def myFunc1_Inner():
        return x + 1        # return value of myFunc1_Inner
    return myFunc1_Inner    # return value of myFunc1

f = myFunc1(10)
print('type of return value is:', type(f), ', value is:', f()) # the value can only be got when the function is called, return value of this function is got
print()

## iterate ?????
def myFunc2(x, y , z):
    def myFunc2_Inner():
        return x + y + z
    return myFunc2_Inner

f1 = myFunc2(1, 2, 3)
f2 = myFunc2(1, 2, 3)
f3 = myFunc2(10, 2, 4)
print('Is f1 == f2:', (f1 == f2)) # KEY: created different instance
print('Is f1 == f3:', (f1 == f3))
print()

# ???? 不太明白闭包： https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000 
def myFunc3():
    L = []
    for i in range(1, 3):
        def myFunc3_Inner():
            L.append(i)
        return L
    return myFunc3_Inner

f11 = myFunc3
f22 = myFunc3
f33 = myFunc3

print(f11())
print(f22())
print(f33())

## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143184474383175eeea92a8b0439fab7b392a8a32f8fa000

## more about int()
# way 1: one parameter
num1 = int('12345')
print(num1)
print()

# way 2: two parameter
num2 = int('20', base = 10)     # change the string to int, who is 十进制
print(num2)
num3 = int('1000', base = 2)    # change the string to int, who is 二进制
print('num3:', num3)
num4 = int('20', base = 16)     # change the string to int, who is 十六进制
print(num4)
num5 = int('20', base = 8)      # change the string to int, who is 八进制
print(num5)

num32 = int('1000', base = 2)               # KEY: equal to this function: change the string to int, who is 二进制
print('num32:', num32)
print()

def int2(x, base = 2):                      # KEY: equal to this function
    return int(x, base)
num33 = int2('1000')
print('num33:', num33)

## partical function
import functools
int2_ = functools.partial(int, base = 2)    # KEY: equal to this function
num34 = int2_('1000')
print('num34:', num34)

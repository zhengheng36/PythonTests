## 命名关键字参数

## Basic
def my_funct_Star(**kw):    # the function only accept dictionary with both 'A' and 'B' as keys
    if 'A' in kw:
        if 'B' in kw:
            print(kw['A'])
            print(kw['B'])
        else:
            print('(Found A, not found B)')
    else:
        print('(Not found A)')

print('For A=100, B= 200, C=23, D= 99:')
my_funct_Star(A=100, B= 200, C=23, D= 99)

print('For C=23, D= 99:')
my_funct_Star(C=23, D= 99)

print('For A=100, D= 99:')
my_funct_Star(A=100, D= 99)

print('For A=100:')
my_funct_Star(A=100)

print('For A=100, B= 200:')
my_funct_Star(A=100, B= 200)

## Star: ??????????????????????????????????????
# print()
# def my_funct_Star_2(*, A, B):
#     print(type(A), A.value)
#     print(type(B), B.value)

# my_funct_Star_2(A='100', B= '200')



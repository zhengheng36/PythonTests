## os command used in Python
## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431925324119bac1bc7979664b4fa9843c0e5fcdcf1e000

import os

print('os.name:', os.name) # 'nt' is windows
print()

#print(os.uname()) # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
print()

print('os.environ:', os.environ)
print()

print('os.environ.get(\'PATH\'):', os.environ.get('PATH'))
print()

print('os.path.abspath(\'.\')', os.path.abspath('.'))
print()

# show all .py file
print('Show all .py file:', [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
print()

## file combine, rename... TBD


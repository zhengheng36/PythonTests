## IO in memoery: StringIO and BytesIO
## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431918785710e86a1a120ce04925bae155012c7fc71e000


## StringIO
from io import StringIO

# example1:
f1 = StringIO()
f1.write('Hello')
print(f1.getvalue())
f1.write(' World')
print(f1.getvalue())
print()

# example2:
f2 = StringIO('Hello\nWorld\n')
while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())
print()

## BytesIO
from io import BytesIO

f3 = BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f4.read())

## IO from file:
## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431917715991ef1ebc19d15a4afdace1169a464eecc2000

## basic
print('f.read():')
try:
    # KEY: open file under path with read only
    f = open('E:/AaronZhengSpace/Python/PythonTests/testIO.txt', 'r')
    # f = open('testIO.txt', 'r') # KEY: same as above
    # KEY: read context of the file
    print(f.read())
except Exception as e:
    print('Error:', e)  # Raise Exception if any
finally:
    f.close()
print()

## readline and read(size)
print('f.readlines():')
try:
    f = open('E:/AaronZhengSpace/Python/PythonTests/testIO.txt', 'r')
    ##print(f.readlines())  # f.readlines() will return a list
    for lines in f.readlines():
        print(lines)
except Exception as e:
    print('Error:', e)  
finally:
    f.close()

print()

## simpfier the code
print('with open():')
with open('E:/AaronZhengSpace/Python/PythonTests/testIO.txt', 'r') as f:
    print(f.read())
print()

## open by 'rb'
print('with open() by \'rb\':')
with open('E:/AaronZhengSpace/Python/PythonTests/testIO.txt', 'rb') as f:
    print(f.read())
print()

## write 
try: 
    f = open('E:/AaronZhengSpace/Python/PythonTests/testIO.txt', 'a') # 'a' as write after end. 'w' will overwrite everything
    f.write('This is next line\n')
except Exception as e:
    print('Error', e)
finally:
    f.close()
with open('E:/AaronZhengSpace/Python/PythonTests/testIO.txt', 'rb') as f:
    print(f.read())
print()



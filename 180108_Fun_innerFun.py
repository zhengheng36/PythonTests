# few inner function of python

## abs
print(abs(1.23))
print()

## max
print(max(1, 200, 5, 658, -50))
print(min(1, 200, 5, 658, -50))
print()

## hex
print(hex(255))
print()

## cast
print(int('1243'))
print(int(12.33))
print(str(123.4))
print(float('2.23'))
print(bool('1'))
print()

## fact: 代码越少，开发效率越高
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)
    
print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))
print(fact(100))


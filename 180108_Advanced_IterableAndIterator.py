## 所有可以用for的，都是Iterable
## 所有可以用next的，都是Iterator

# for 其实相当于不断的调用next()

from collections import Iterable
from collections import Iterator

print(isinstance((x for x in range(10)), Iterable))
print(isinstance((x for x in range(10)), Iterator))

print(isinstance([], Iterable))
print(isinstance([], Iterator))
print(isinstance(iter([]), Iterable))
print(isinstance(iter([]), Iterator))

print(isinstance({}, Iterable))
print(isinstance({}, Iterator))

print(isinstance('abc', Iterable))
print(isinstance('abc', Iterator))
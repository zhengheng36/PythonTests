## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431953239820157155d21c494e5786fce303f3018c86000


## a fixed tuple/ a class with only members not methods
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 3)
p2 = Point(-1, 5)
print('p1(%s, %s):' % (p1.x, p1.y))
print('p2(%s, %s):' % (p2.x, p2.y))
print('isinstance(p1, Point):', isinstance(p1, Point))
print('isinstance(p1, tuple):', isinstance(p1, tuple), '\n')

## deque 双向列表：方便在头部和尾部进行操作
from collections import deque
ADeque = deque(['a', 'b', 'c'])
print('ADeque:', ADeque)
ADeque.appendleft('EE')
print('ADeque:', ADeque)
ADeque.append('FF')
print('ADeque:', ADeque)
ADeque.popleft()
ADeque.popleft()
print('ADeque:', ADeque, '\n')

## Counter()
from collections import Counter
ACounter = Counter()
for ch in 'ABCDEFAB':
    ACounter[ch] = ACounter[ch] + 1
print('type(ACount):', type(ACounter), 'ACounter:', ACounter)
print('isinstance(ACounter, dict):', isinstance(ACounter, dict), '\n')

## defaultdict: same as dict, but assign default key for element if not assign
from collections import defaultdict

ADefualtdict = defaultdict(lambda: 'N/A(Default Value Set)')
ADefualtdict['KEY1'] = 100
print('ADefualtdict[\'KEY1\']:', ADefualtdict['KEY1'])
print('ADefualtdict[\'KEY2\']:', ADefualtdict['KEY2'], '\n')

## Order dic based on INSERTING orders
from collections import OrderedDict

ADic = dict([('a', 1), ('c', 3), ('b', 2)])
ADicAfterOrd = OrderedDict(ADic)
print('ADicAfterOrd:', ADicAfterOrd, '\n')



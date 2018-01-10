## ref:  https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143200162233153835cfdd1a541a18ddc15059e3ddeec000


# KEY1: 定义并不能循环出来，要结合for使用
# KEY2: 会一直循环，停不下来，用Ctrl + C来停止
import itertools, time

## count()
# ATest1 = itertools.count(1)
# for n in ATest1:
#     # print(ATest1) # not get the values
#     print(n)

## cycle()
# ATest2 = itertools.cycle('123')
# for ch in ATest2:
#     print(ch)
#     time.sleep(0.5)

## repeat()
# ATest3 = itertools.repeat('ABC', 4) # KEY, repeat the whole thing inside ''
# for ch3 in ATest3:
#     print(ch3)
#     time.sleep(0.5)

## takewhile()
# ATest4 = itertools.count(1)
# ns = list(itertools.takewhile(lambda x: x < 10, ATest4))
# print(ns)

## chain(): stopable
# ATest5 = itertools.chain('ABC', 'DEF')
# for ch5 in ATest5:
#     print(ch5)
#     time.sleep(0.5)

## groupby()
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

print()

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))


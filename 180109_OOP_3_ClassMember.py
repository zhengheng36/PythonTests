## Class member will be visable to all instance, should be very careful

class MyC(object):
    name = 'ABC'

InMyC1 = MyC()
print(InMyC1.name)

InMyC2 = MyC()
print(InMyC2.name)

InMyC3 = MyC()
InMyC3.name = 'AaronZheng'      # 用相同的变量名会屏蔽掉类属性
print(InMyC3.name)

InMyC4 = MyC()
print(InMyC4.name)
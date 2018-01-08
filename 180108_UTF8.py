# Python中的编码问题

print('证明Python也是可以使用其他语言的，比如说，中文')

# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A')) # char --> ASCII
print(chr(65))  # ASCII --> char

print(ord('郑'))
print(ord('恒'))
print(chr(24658))

# 可以使用16位来表示
print('\u4e2d\u6587')

# 可以改成想要的编码
print('郑恒'.encode('utf-8'))
print(b'\xe9\x83\x91\xe6\x81\x92'.decode('utf-8'))

# length
print('the length of ABC is:', len("ABC"))

# 后面带参数的占位符: if you are not very sure, use %s always
# %% use to display one % 
outputStr = 'Hello %s, your phone number is: %d, and your amout right now is: %f %%' % ('AZ', 613600, 12.11)
print(outputStr)

# the other way of doing so is here, but not recommand
outputStr2 = 'Hello {0}, your money is: {1:.1f}%'.format('AZ', 17.11)
print(outputStr2)







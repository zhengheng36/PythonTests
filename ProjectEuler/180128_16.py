# Power digit sum
# Problem 16 
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 21000?




n = 1000
numPow = 1

sumNum = 0

while n != 0:
    numPow *= 2
    n -= 1

print(numPow)

strNum = str(numPow) # KEY step
print(strNum)

for i in strNum:
    sumNum = sumNum + int(i)

print(sumNum)

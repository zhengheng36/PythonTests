# two loop conditions

# range
listNum = list(range(1, 100)) # make the range to be a list
print('Result of range 1 - 100 is:', listNum)

# for
sumUp = 0
for num in listNum:
    sumUp = sumUp + num

print('sumUp is:', sumUp)

# while
sumUp2 = 0
cnt = 0
while cnt < len(listNum):
    sumUp2 = sumUp2 + listNum[cnt]
    cnt = cnt + 1
else:
    print('sumUp2 is:', sumUp2)
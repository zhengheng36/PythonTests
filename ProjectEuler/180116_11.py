# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

ListNumStr = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
''' # KEY: ''' must not in any lines of numbers

## make the string into a 2D array: the terminater in ListNumStr is '\n'
ListNum = []


totalLen = len(ListNumStr)

indexCnt = 0

## KEY: change string chars into 2D ListNum
subList = []
while True:
    if indexCnt == totalLen:
        break
        
    # if meet the end of line, add current subList into ListNum and then create a new subList
    if ListNumStr[indexCnt] == '\n':
        if len(subList) != 0:
            ListNum.append(subList)
            subList = []
        indexCnt = indexCnt + 1
        continue
    # skip blank char
    elif ListNumStr[indexCnt] == ' ':
        indexCnt = indexCnt + 1
        continue
    # get continue two char as int and add into subList
    else:
        stringNum = ListNumStr[indexCnt] + ListNumStr[indexCnt + 1]
        num = int(stringNum)
        subList.append(num)
        indexCnt = indexCnt + 2
        continue

# Test: TEST GOOD
# print()
# print(ListNum)
# print()
# for subListTmp in ListNum:
#     print(subListTmp)
# print()


# KEY: the function definition must before function call
# function1: left <-> right
def GetLargestInLeftRight(ListNum):
    sumMax = 0

    for subList in ListNum:
        startIndexCnt = 0
        sumTmp = 0
        while True:
            if startIndexCnt == (20 - 3):
                break
            sumTmp = subList[startIndexCnt] * subList[startIndexCnt + 1] * subList[startIndexCnt + 2] * subList[startIndexCnt + 3]
            if sumTmp > sumMax:
                sumMax = sumTmp
                print('%s,%s,%s,%s' % (subList[startIndexCnt], subList[startIndexCnt + 1], subList[startIndexCnt + 2], subList[startIndexCnt + 3]))
            
            startIndexCnt = startIndexCnt + 1

    return sumMax

# function2: top <-> down
def Rotate2DList(ListNum):
    ListNumNew = [] 
    for i in range(0, 20): # KEY: max i can get is 19
        subListNew = []
        for j in range(0, 20):
            subListNew.append(ListNum[j][i])

        ListNumNew.append(subListNew)

    return ListNumNew

        

def GetLargestInTopDown(ListNum):
    ListNumRotated = Rotate2DList(ListNum)
    return GetLargestInLeftRight(ListNumRotated)

# function3: diagonally: top left to down right
def GetLargestDiagonally1(ListNum):
    sumMaxDia1 = 0
    sumMaxDia1Tmp = 0
    for j in range(0 , 17):
        for i in range(0, 17):
            sumMaxDia1Tmp = ListNum[j][i] * ListNum[j+1][i+1] * ListNum[j+2][i+2] * ListNum[j+3][i+3]
            if sumMaxDia1Tmp > sumMaxDia1:
                sumMaxDia1 = sumMaxDia1Tmp
                print('%s,%s,%s,%s' % (ListNum[j][i], ListNum[j+1][i+1], ListNum[j+2][i+2], ListNum[j+3][i+3]))

    return sumMaxDia1

# function4: diagonally: top right to down left
def GetLargestDiagonally2(ListNum):
    sumMaxDia2 = 0
    sumMaxDia2Tmp = 0
    for j in range(0 , 17):
        for i in range(3, 20):
            sumMaxDia2Tmp = ListNum[j][i] * ListNum[j+1][i-1] * ListNum[j+2][i-2] * ListNum[j+3][i-3]
            if sumMaxDia2Tmp > sumMaxDia2:
                sumMaxDia2 = sumMaxDia2Tmp
                print('%s,%s,%s,%s' % (ListNum[j][i], ListNum[j+1][i-1], ListNum[j+2][i-2], ListNum[j+3][i-3]))

    return sumMaxDia2


# main: 
sumMaxLeftRight = GetLargestInLeftRight(ListNum)
print('max sum of left and right:', sumMaxLeftRight)

# print('\nTest rotated ListNum')
# TestListRotated = Rotate2DList(ListNum)
# print(TestListRotated)
# print(list(range(0, 20)))

sumMaxTopDonw = GetLargestInTopDown(ListNum)
print('max sum of top and down:', sumMaxTopDonw)

sumMaxDia1 = GetLargestDiagonally1(ListNum)
print('max sum sumMaxDia1:', sumMaxDia1)

sumMaxDia2 = GetLargestDiagonally2(ListNum)
print('max sum sumMaxDia2:', sumMaxDia2)





## Notes: take a lot of time to think about it




## useless code:

# KEY: way of getting int from two chars: https://stackoverflow.com/questions/5239071/creating-one-string-from-two-in-python
# print(ListNumStr[0])
# print(ListNumStr[1])
# print(ListNumStr[2])
# print(ListNumStr[3])
# print(ListNumStr[4])
# print(ListNumStr[5])
# print(ListNumStr[6])
# print(ListNumStr[7])
# print(ListNumStr[8])

# print()
# stringNum = ListNumStr[2] + ListNumStr[3]
# num = int(stringNum)
# print(num)

# stringNum = ListNumStr[7] + ListNumStr[8]
# num = int(stringNum)
# print(num)



## KEY: change string chars into list of numbers 
# while True:
#     if indexCnt == totalLen:
#         break
        
#     if ListNumStr[indexCnt] == '\n' or ListNumStr[indexCnt] == ' ':
#         indexCnt = indexCnt + 1
#         continue
#     else:
#         stringNum = ListNumStr[indexCnt] + ListNumStr[indexCnt + 1]
#         num = int(stringNum)
#         ListNum.append(num)
#         indexCnt = indexCnt + 2




##ListNumStr1 = '''08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''


# lenTotal = len(ListNumStr1)

# i = 0
# while True:
#     # Stop when reaching the end of ListNumStr
#     if i + 1 == lenTotal:
#         break
    
#     subList = []
#     while True:
#         # add the first one into new subList first
#         subList.append(int(ListNumStr1[i]))
#         i = i + 1

#         # condition to stop buidling this sublist
#         if i % 20 == 0:
#             break

#         # add the item into sublist
#         subList.append(int(ListNumStr1[i]))
#         i = i + 1
    
#     # add the subList into the ListNum
#     ListNum.append(subList)

# print(ListNum)

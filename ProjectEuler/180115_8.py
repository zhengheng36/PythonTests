# Largest product in a series
# Problem 8 
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450

# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

OriginalString = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

#print(OriginalString)

NumList = []

for ch in OriginalString:
    if ch != '\n':
        NumList.append(int(ch)) # change string list to a int list with numbers

# # Check if size is correct
# print(NumList)
# print(len(NumList))

MaxProduct = 0
AD_DIGIAL = 13
END_CONDITION = len(NumList) - 13 - 1
#print(END_CONDITION)

IndexOffset = -1
while True:
    IndexOffset = IndexOffset + 1
    if IndexOffset == END_CONDITION:    # Notice end condition to avoid 'out of range'
        break
    else:
        indexCnt = 0
        tmpPro = 1
        while indexCnt < AD_DIGIAL:
            tmpPro = tmpPro * NumList[indexCnt + IndexOffset]
            indexCnt = indexCnt + 1
        if tmpPro > MaxProduct:
            MaxProduct = tmpPro

    
print(MaxProduct)

## TEST GOOD: very faster. 


## tests for numbers in different line
# TestList1 = [1, 2, 3, 4]
# print(TestList1)
# TestTuple1 = (1, 2, 3, 4)
# print(TestTuple1)

# TestString1 = '71636269561882670428252483600823257530420752963450'
# print(TestString1)
# print(TestString1[0])
# print(TestString1[1])
# print(TestString1[2])
# print()

# ### KEY: ref: https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string
# TestString2 = """1
# 2
# 3
# 45"""
# print(TestString2)
# print(TestString2[0])
# print(TestString2[1])
# print(TestString2[2])

### Check the end of a list
# ListForCheck = [1, 2, 3]
# print(ListForCheck[3])



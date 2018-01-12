# # Sum square difference
# # Problem 6 
# # The sum of the squares of the first ten natural numbers is,

# # 12 + 22 + ... + 102 = 385
# # The square of the sum of the first ten natural numbers is,

# # (1 + 2 + ... + 10)2 = 552 = 3025
# # Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# # Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from datetime import datetime
print(datetime.now())
def SeqOfSum(num):
    total1 = 0
    while True:
        if num == 0:
            break
        total1 = total1 + num * num
        num = num - 1
    return total1
    

def SumOfSeq(num):
    total2 = 0
    while True:
        if num == 0:
            break
        total2 = total2 + num
        num = num - 1
    return total2 * total2


result = SumOfSeq(100) - SeqOfSum(100)
print(result)
print(datetime.now())

## It: it seems a little faster than C code in this way


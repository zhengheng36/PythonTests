# ## 

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.


MaxNumberCnt = 0
MaxBeginNum = 0
StartNum = 1000000

while StartNum != 1:
    ListNumbers = []
    BeginNum = StartNum
    while BeginNum != 1:
        if BeginNum % 2 == 0:
            BeginNum = BeginNum / 2
            ListNumbers.append(BeginNum)
        else:
            BeginNum = BeginNum * 3 + 1
            ListNumbers.append(BeginNum)

    if MaxNumberCnt < len(ListNumbers):
        MaxNumberCnt = len(ListNumbers)       
        MaxBeginNum = StartNum  
    
    print('CurrTestNumber %s, NumbCurrChain %s, MaxNumOfChain %s, MaxBegin %s' % (StartNum, len(ListNumbers), MaxNumberCnt, MaxBeginNum))

    StartNum = StartNum - 1


print(StartNum)

## the program above can give out the correct answer, but it will take a whiel

## the solution inspire me not to use a list, but simply record the number on the currrent chain is easier

## the faster way of using number is not by while but by range(1, 1000000)

## the other way I can think of to do so is by creating a BTree
## if the node value is less then 1000000 than created right and left child node with value(Node*2 and (Node - 1)/3)
## so BTREE will stop generateing new node when current node is finally bigger than 1000000. 
## Then we got the answer.



## Better Python Example
# results = {}

# def collatz(a):
#     counter = 1
#     b = a
#     while b != 1:
#         if b % 2 == 0:
#             counter += 1
#             b //= 2
#         else:
#             counter += 1
#             b = 3 * b + 1
#     results[a] = counter

# for c in range(1,1000000):
#     collatz(c)
# print(max(results, key = lambda k: results[k]))




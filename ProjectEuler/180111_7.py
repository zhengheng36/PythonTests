# 10001st prime
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


def GetTheNthPrimeNum(n):
    CntTotalNum = 1
    num = 2
    while True:
        cnt = 2
        num = num + 1
        while cnt < num:
            if num % cnt == 0:
                break
            cnt = cnt + 1
            pass

        if cnt == num:  # find a prime
            CntTotalNum = CntTotalNum + 1

        if CntTotalNum == n:    # get the last number
            break
    return num

print(GetTheNthPrimeNum(10001))

## It will take hours to finish it


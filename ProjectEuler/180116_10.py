# Summation of primes
# Problem 10 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def GetPrimeList(AListPrime, underCnt):
    PrimeNum = 2
    CheckDiv = 2

    while True:
        if PrimeNum == underCnt:
            break

        # check if PrimeNum is PrimeNum
        CheckDiv = 2
        while True:
            if PrimeNum % CheckDiv == 0:
                break

            if PrimeNum == CheckDiv:
                break

            CheckDiv = CheckDiv + 1

        # record the number if it is prime
        if  PrimeNum == CheckDiv:
            AListPrime.append(PrimeNum)

        # check the next one
        PrimeNum = PrimeNum + 1
        print('Test:', PrimeNum)


sumRet = 0
PrimeListTmp = []
GetPrimeList(PrimeListTmp, 2000000)
##print(PrimeListTmp)

for num in PrimeListTmp:
    sumRet = sumRet + num


print(num)

    
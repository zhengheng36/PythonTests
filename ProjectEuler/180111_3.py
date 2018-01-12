# //Largest prime factor
# 	//Problem 3
# 	//The prime factors of 13195 are 5, 7, 13 and 29.
# 	//
# 	//What is the largest prime factor of the number 600851475143 ?

def GetListPrimeNums(L):
    ListPrimeNew = []
    for num in L:
        Cnt = 2
        while Cnt < num:
            if  num % Cnt == 0:
                break
            Cnt = Cnt + 1    
        if Cnt == num:
            ListPrimeNew.append(Cnt)
    return ListPrimeNew


##print(GetListPrimeNums(list(range(1, 10000)))) ## Test Only

ListOfPrimeNumbers = GetListPrimeNums(list(range(1,10000)))

ListAnswer = []
Totoal = 600851475143

while True:
    for primeNum in ListOfPrimeNumbers:
        if Totoal % primeNum == 0:
            ListAnswer.append(primeNum)
            Totoal = Totoal / primeNum
            break
    if Totoal == 1:
        break

print(ListAnswer)

## It: the speed is not too slow for me to notice. And it is much less code in python instead of in C


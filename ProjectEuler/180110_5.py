# # Smallest multiple
# # Problem 5 
# # 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# # What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def IsEvenlyDivisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

for num in range(1, 5000000000000):
    if IsEvenlyDivisible(num):
        print(num)
        break


# answer: 232792560
## much faster in C: C:\APRG\FIX Platform\src\tests\TestEnqueueInstruction\TestEntry\180110_ForFunOnly.c: Test3

# # Tests:
# for i in range(21):
#     print(i)
# for i in range(1, 21):
#     print(i)



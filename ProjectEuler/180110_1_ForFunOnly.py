# Multiples of 3 and 5
# Problem 1 
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.


def IsTheNumberGood(a):
    if a % 3 == 0:
        return True
    elif a % 5 == 0:
        return True
    else:
        return False

sum = 0
for n in range(1, 1000):
    if IsTheNumberGood(n) == True:
        sum = sum + n

print(sum)

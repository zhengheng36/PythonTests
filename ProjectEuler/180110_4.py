# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def IsPalindrome(n):
    strNew = ''
    strOld = str(n)
    length = len(strOld)
    while length > 0:
        strNew = strNew + strOld[length - 1]
        length = length - 1
    NumNew = int(strNew)
    return (NumNew == n)

result = 0

for a in range(100, 999):
    for b in range(100, 999):
        tmp = a * b
        if IsPalindrome(tmp):
            if tmp > result:
                result = tmp

print(result)


# KEY: LEARN to reverse string!!!
StrNumTest = '12345'
print(StrNumTest[::-1]) # [start:end:reverse]
print(StrNumTest[::1])  # [start:end:get every one]
print(StrNumTest[::2])  # [start:end:get every 2]



            






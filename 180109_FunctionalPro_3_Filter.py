## filter function has the same input parameter as map
## based on function condition, 
## KEY: if function return True, the element will be kept. Otherwise, discarded

def filter_fun_OneInputPara(x):
    return x % 2 == 1   # only return True when x is odd

# KEY: as map(), need to list() 
ListNew = list(filter(filter_fun_OneInputPara, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(ListNew)

## practice: https://stackoverflow.com/questions/199184/how-do-i-check-if-a-number-is-a-palindrome
def Is_palindrom(num):
    strNum = str(num) # convert the int to string
    lenNum = len(strNum)
    cnt = 0
    strNew = ''
    while lenNum > 0:  # reverse the string 
        strNew = strNew + strNum[lenNum - 1]
        lenNum = lenNum - 1

    numNew = int(strNew)    # convert the string back to int
    if numNew == num:       # compare the ints and return bool
        return True
    else:
        return False

print(list(filter(Is_palindrom, range(1, 1000))))
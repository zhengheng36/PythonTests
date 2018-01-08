## def function and check input parameter

## basic
def my_abs(inputNum):
    if not isinstance(inputNum, (int, float)): # KEY
        raise TypeError("The type of input number should be 'int' or 'float'")
    else:
        if inputNum > 0:
            return inputNum, inputNum
        else:
            return inputNum, -inputNum


GetResultOfInputNum = my_abs(-9)
print('GetResultOfInputNum is:', type(GetResultOfInputNum), GetResultOfInputNum) # KEY: the output shows, the return valuse is a tuple, a list whose elements cannot be changed
print("InputNum is: {0}, outputNum is: {1}".format(GetResultOfInputNum[0], GetResultOfInputNum[1]))

print()             

## Test if function call can change input paramet
def tryToChangeInputPara(inputNum2):
    inputNum2 = inputNum2 + 1
    return inputNum2

InputNum2_Def = 10
GetResultOfInputNum2 = tryToChangeInputPara(InputNum2_Def)
print('Input InputNum2_Def is:', InputNum2_Def)   # KEY: the inner function cannot change the value of input parameter
print('Output GetResultOfInputNum2 is:', GetResultOfInputNum2) # get the changed value from output

        
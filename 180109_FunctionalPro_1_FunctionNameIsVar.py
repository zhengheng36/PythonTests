## 函数名也是变量
## 把函数名当成传入参数的函数，称为：高阶函数 Higher-order function


## function name can be passed as variable
print('abs(-10):', abs(-10))
f = abs
print('f(-10):', f(-10))

## pass function name as input parameter
def my_fun(funcName):   # higher-order function
    print('funcName is:', type(funcName), 'funcName(-10) is', funcName(-10))

funcNameTmp = abs
my_fun(funcNameTmp)


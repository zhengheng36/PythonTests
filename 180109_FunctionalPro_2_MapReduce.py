## map and reduce function in Python

## map
## format: ListNew = List(map(functionName, [param1, param2, param3, ...]))
## it:      list(map(funcName, [a, b, c, d, e])) = [funcName(a), funcName(b), funcName(c), funcName(d)]
#           pass all elements in second parameters into functionName(ONLY ONE input parameter)
##          then generated a list of results

def my_fun(x):
    return x * x

ListOld = [my_fun(1), my_fun(2), my_fun(3), my_fun(4), my_fun(5)]
print('ListOld is: ', ListOld)

ListNew = list(map(my_fun, [1, 2, 3, 4, 5]))
print('ListNew is: ', ListNew)

## reduce
## it:    reduce(funName, [a, b, c, d]) = funName(funName(funName(a, b),c), d)
from functools import reduce # need to import 

def my_fun2(x, y):
    return x + y

ResultOld = my_fun2(my_fun2(my_fun2(1, 2), 3), 4)
print('ResultOld is:', ResultOld)

ResultNew = reduce(my_fun2, [1, 2, 3, 4])
print('ResultNew is:', ResultNew)

## MapReduce: ref https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf 
def fun_OneParam(x):
    return x + 1

def fun_TwoParam(x, y):
    return x * y

print(reduce(fun_TwoParam, list(map(fun_OneParam, [1, 2, 3, 4, 5]))))
# equal to: 1. make a list from 1, 2, 3, 4, 5, witn one more increase
#           2. based on 2, 3, 4, 5, 6, mutiple pervious two and calculate restult
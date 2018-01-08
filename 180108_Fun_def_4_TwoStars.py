## Name(**inputPara) example

## Original example
def my_fun_OneStartInputPara_Dic(inputParamList): # input parameter is a dictionary
    for num in inputParamList:
        print(num)
        
print('Example1:')
my_fun_OneStartInputPara_Dic({'A': 1, 'B': 2, 'C': 4})

## One Star Example: equal to the first one, but simpler
def my_fun_OneStartInputPara(**inputParam): # input parameter is a changable dictonary
    for num in inputParam:
        print(num)
        
print('Example2:')
my_fun_OneStartInputPara(A=10, B=20, C=30)  # KEY way1: the way of input key-value pair

print('Example3: useful')
dicIn = {'a': 9, 'b': 10, 'c': 100}
my_fun_OneStartInputPara(**dicIn)           # KEY way2: the way of input key-value pair
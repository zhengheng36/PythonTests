## Name(*inputPara) example

## Original example
print('Exmaple1:')
def my_fun_OneStartInputPara_List(inputParamList): # input parameter is a list(or tuple)
    for num in inputParamList:
        print(num)
        
my_fun_OneStartInputPara_List([1, 2, 3, 4, 5, 6])

## One Star Example: equal to the first one, but simpler
print('Exmaple2:')
def my_fun_OneStartInputPara(*inputParam): # input parameter is a changable list
    for num in inputParam:
        print(num)
        
my_fun_OneStartInputPara(1, 2, 3, 4, 5, 6)

print('Exmaple3: very useful way of doing it')
inNum = [5, 6, 7, 8]
my_fun_OneStartInputPara(*inNum)
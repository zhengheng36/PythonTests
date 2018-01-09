## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191375461417a222c54b7e4d65b258f491c093a515000


## basic: try-except-else-finally
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')                # KEY: the prog will keep executing to the end
print()


## Learn error infor from call stacks
# def func1(s):
#     return 10 / s

# def func2(s):
#     return func1(s)

# ret1 = func2(0)
# # from top to bottom
# # # # # Traceback (most recent call last):  File "C:\Users\Aaron.Zheng\.vscode\extensions\ms-python.python-0.9.1\pythonFiles\PythonTools\visualstudio_py_launcher_nodebug.py", line 74, in run
# # # # #     _vspu.exec_file(file, globals_obj)
# # # # #   File "C:\Users\Aaron.Zheng\.vscode\extensions\ms-python.python-0.9.1\pythonFiles\PythonTools\visualstudio_py_util.py", line 119, in exec_file
# # # # #     exec_code(code, file, global_variables)
# # # # #   File "C:\Users\Aaron.Zheng\.vscode\extensions\ms-python.python-0.9.1\pythonFiles\PythonTools\visualstudio_py_util.py", line 95, in exec_code
# # # # #     exec(code_obj, global_variables)
# # # # #   File "e:\AaronZhengSpace\Python\PythonTests\180109_RaiseErr_1_Basic.py", line 28, in <module>
# # # # #     ret1 = func2(0)
# # # # #   File "e:\AaronZhengSpace\Python\PythonTests\180109_RaiseErr_1_Basic.py", line 26, in func2
# # # # #     return func1(s)
# # # # #   File "e:\AaronZhengSpace\Python\PythonTests\180109_RaiseErr_1_Basic.py", line 23, in func1
# # # # #     return 10 / s
# # # # # ZeroDivisionError: division by zero
print()

## logging error
# import logging
# def func3(s):
#     return 10 / s

# def func4(s):
#     return func3(s)

# def main():
#     try:
#         func4(0)
#     except Exception as e:
#         logging.exception(e)    # ??? Log Location??
# main()
# print()

## raise error
def func5(s):
    try:
        if s == 0:
            print("Raise Error")
            raise ValueError('Value is invalid', s)
        else:
            return 10 / s 
    except ValueError as e:
        print('Error Catched:', e)    
    finally:
        print('END')
        
func5(0)

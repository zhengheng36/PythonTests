## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000

DIC_TEST = {'ABC': 10, 'DEF': 20, 'GHI': 30}

## pickle: only used inside Python. Better to use JSON next for universal 
import pickle

print('pickle.dump:')
try:
    f = open('testPickle.txt', 'wb')
    pickle.dump(DIC_TEST, f)            # KEY: add dic into txt using pickle
except Exception as e:
    print('Error', e)
finally:
    f.close()
    print('(END)')
print()

# read 
print('pickle.load:')
with open('testPickle.txt', 'rb') as f:
    Dic_load = pickle.load(f)
    print(Dic_load)
print()

## JSON
import json

print('json.dumps():')
strGet = json.dumps(DIC_TEST)
print(strGet)

print('json.loads():')
dicGet = json.loads(strGet)
print(dicGet)

## JSON advance: JSON a class: TBD

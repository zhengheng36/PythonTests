## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186739713011a09b63dcbd42cc87f907a778b3ac73000
## Instance can add methods/members for itself

class BaseClass(object):
    def Run(self):
        print('Running..')
        print()


Obj1 = BaseClass()
Obj1.Run()
print()

# KEY: add extra members for this instance only
Obj1.name = 'Obj1'                      
print('Print Obje1.name:', Obj1.name)
print()

# KEY: add extra method for this instance
from types import MethodType       
def forObj1Only(self):
    print('Test: forObj1Only')

Obj1.Obj1Method = MethodType(forObj1Only, Obj1)

Obj1.Obj1Method()
print()

Obj2 = BaseClass()
####print('Print Obje2.name:', Obj2.name) # KEY: cannot work, because Obj2 has not member of 'name'

# KEY: add extra member for the whole class, so that all the instance will apply this member
BaseClass.phone = 12356

print('Print Obj1.phone:', Obj1.phone)
print('Print Obj2.phone:', Obj2.phone)
print()


## restrict what members can be added into instance in class side: __slots__
## (See reference)

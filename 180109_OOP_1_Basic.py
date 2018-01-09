## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431864715651c99511036d884cf1b399e65ae0d27f7e000

## Object Oriented Programming，简称OOP


# KEY: define a class: if not input parameter for class, keep 'object'
class NewClass(object):

    # KEY: Construct Function
    def __init__(self, name, phone):
        self.__name = name              # KEY: if a member define as '__XXX' it is private, cannot be reached from outside
        self.__phone = phone
    
    # KEY:  the only difference between function and class method is: 
    #       class method will have first input parameter as 'self'
    def PrintInfo(self):
        print('Name:', self.__name, ', Phone:', self.__phone)

    # KEY: use __ 达到封装的效果
    def get_name(self):
        return self.__name


InstanceNewClass1 = NewClass('AZ', 123)
InstanceNewClass1.PrintInfo()
print()

print('Display Name:', InstanceNewClass1.get_name())
print()

# KEY: get class attr
print('NewClass has attr:', dir(NewClass))
print()
print('Is get_name in NewClass:', hasattr(NewClass, 'get_name')) # KEY: must use ''
print()

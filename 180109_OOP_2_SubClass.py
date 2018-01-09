## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431865288798deef438d865e4c2985acff7e9fad15e3000

## Basic
class Animal(object):
    def Run(self):
        print('Animal is running')

class Dog(Animal):
    pass

class Bear(Animal):
    def Run(self):
        print('Bear is running')

ADog = Dog()
ADog.Run()                  # KEY: if subclass do not have same method, base class method will be called
ABear = Bear()          
ABear.Run()                 # KEY: if subclass do not have same method, sub class method will be called
print()

## Instance Check
AAnimal = Animal()
print('is ADog an instance of class Animal:', isinstance(ADog, Animal))
print('is ADog an instance of class Dog:', isinstance(ADog, Dog))
print()
print('is AAnimal an instance of class Animal:', isinstance(AAnimal, Animal))
print('is AAnimal an instance of class Dog:', isinstance(AAnimal, Dog))
print()

## 多态：不用太在乎传入的是什么，像鸭子就按照鸭子来对待: file-like object
def Run_Twice(Animal):
    Animal.Run()
    Animal.Run()

Run_Twice(AAnimal)
Run_Twice(ADog)         # the pass in parameter is like Animal, so it can be passed in
Run_Twice(ABear)        # the Bear() will have overwrite Run
print()


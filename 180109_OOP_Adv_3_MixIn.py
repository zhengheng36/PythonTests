

## MixIn: one class can be subClass of more than one BaseClass: (Jave not apply)


class BaseClass1(object):
    def __init__(self):
        print('This is BaseClass1')

class BaseClass2(object):
    def __init__(self):
        print('This is BaseClass2')

class Dog(BaseClass1, BaseClass2):
    def __init__(self):
        print('This is Dog')

ObjDog = Dog()
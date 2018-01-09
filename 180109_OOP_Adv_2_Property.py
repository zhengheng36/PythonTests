
## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000 
## use property to set and get members of a class

class TestPropertyClass(object):

    @property                           # KEY: just like get
    def score(self):
        return self._score  #get

    @score.setter                       # KEY: just like set
    def score(self, value):
        if value > 100 or value < 0:
            print('Cannot set score')
            return
        else:
            self._score = value #set


Obj1 = TestPropertyClass()
Obj1.score = 90
print(Obj1.score)

# Obj2.score = 150
# print(Obj2.score)

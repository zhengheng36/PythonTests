
## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431845183474e20ee7e7828b47f7b7607f2dc1e90dbb000
## Call different Moudle

## basic 
import TestModule
print()

TestModule.Display()
print()

## advance with sys input parameter
import TestModule_Ad

## defined private method:
# there is not private method in Python. 
# In order to 封装, set private method name begin with '_' like '_InnerCaller'
# Try to avoid called method name begine with '_' to avoid calling private function

def _shouldNotBeCalledOutside(): # _: 虽然我是公开的，但是，请把我视为私有变量，不要随意访问
    print('private function _shouldNotBeCalledOutside is called by public function')

def PublicFunc():
    _shouldNotBeCalledOutside() 
    
# only way to execute _shouldNotBeCalledOutside is by calling PublicFunc
PublicFunc()
print()

## import third party Module: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186362353505516c5d4e38456fb225c18cc5b54ffb000

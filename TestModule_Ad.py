## this .py will be called by 180109_Module_1_CallModule.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '                       # Module Comments

__author__ = 'Aaron Zheng'              # Module Creator

import sys                              # can support one or two input parameter

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# this will execute without calling special methods
print('TestModule.py is called')
print()
test()
print()
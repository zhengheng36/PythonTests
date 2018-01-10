## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431928972981094a382e5584413fa040b46d46cce48e000


## 不想使用锁，所以每个线程内，使用局部变量
## 并且，在外部，可以有一个全局变量来访问任意线程中的任意局部变量
## --> 使用一个全局的dic。dic的key是线程名称，dic的value，是局部变量（因为key唯一，所以只支持每个线程有一个局部变量）
##          eg. LocalVarInThread1 = global_dic[threading.current_thread().name]
##          eg. LocalVarInThread2 = global_dic[threading.current_thread().name]

## --> 更好的方法：使用 ThreadLocal对象。认为是一个可以储存重复key 的 global dic. 
##                ad：
##                      - 每个线程有自己的局部变量，不用使用锁
##                      - 可以通过访问ThreadLocal来访问任意线程的任意局部变量
##                      - 可以有多个线程局部变量

import threading

global_ThreadLocal = threading.local()

def PrintThreadLocalVar():
    print('Tthread %s score %s' % (global_ThreadLocal.name, global_ThreadLocal.score))

def ThreadProc(score):
    print('Thread %s start' % threading.current_thread().name)
    # KEY: think in this way: currentThread.name and currentThread.score.
    #                    ???  so that you cannot mix it and we can visit this global_ThreadLocal anyway, with correct name
    #                    !!!  主要解决在一个线程中，各个函数之间传递数据的问题
    global_ThreadLocal.name = threading.current_thread().name
    global_ThreadLocal.score = score # KEY: create a new local variable and only attach to this thread, no lock need
    PrintThreadLocalVar()
    print('Thread %s end' % threading.current_thread().name)

thread1 = threading.Thread(target=ThreadProc, name='SubThread1', args=(5,))
thread2 = threading.Thread(target=ThreadProc, name='SubThread2', args=(6,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print()
print('global_ThreadLocal attrib: ', dir(global_ThreadLocal))




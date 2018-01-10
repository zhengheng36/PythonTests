## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192823818768cd506abbc94eb5916192364506fa5d000


## Most of time, making use of 'threading'
# import threading
# import time             # KEY for sleep

# def ThreadProc():
#     print('Thread %s is starting...' % threading.current_thread().name) # KEY: way of getting current thread name
#     n = 0 
#     while n < 5:
#         print('Thread %s is working on job %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#         n = n + 1
#     else:
#         print('Thread %s finished working, end' % threading.current_thread().name)


# print('Test Begin....')
# print('Current MainThread is: %s' % threading.current_thread().name)

# # KEY: define
# NewTread = threading.Thread(target = ThreadProc, name = 'SubThread')

# # KEY: start
# NewTread.start()

# # KEY: wait for end
# NewTread.join()

# print('Thread %s finished working, end' % threading.current_thread().name)







## lock: 
##      - the difference between processes and threads is, threads look into the same memory but processes look into different memory
##      - need a lock to protect data within threads

import threading

a = 1       # KEY: !! way of sharing a common varialbe is by defined at top. used with 'global XXX'
b = 2

# KEY: define a lock
lock = threading.Lock()

def SharedThreadProc():
    global a
    global b
    print('Thread %s start...' % threading.current_thread().name)
    # KEY: acquire a lock
    lock.acquire()
    try:
        a = a + 1
        b = b + 1
        print('Thread %s Do Work: a is: %s, b is: %s' % (threading.current_thread().name, a, b))
    finally:
        # KEY: release a lock
        lock.release()
    print('Thread %s finished, end' % threading.current_thread().name)
    

print('Current MainThread is: %s' % threading.current_thread().name)

NewThread2 = threading.Thread(target=SharedThreadProc, name='Sub-Thread1')
NewThread3 = threading.Thread(target=SharedThreadProc, name='Sub-Thread2')

NewThread2.start()
NewThread3.start()

NewThread2.join()
NewThread3.join()

print('Thread %s finished, end' % threading.current_thread().name)








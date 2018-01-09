## Created mutiple process by Python
## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000

## Created undre Unix and Linux
## TBD, cannot work under windows

## Created one child process in windows:
# from multiprocessing import Process
# import os

# def newProcessProc(name):   # job for new process
#     print('     Run child process name:%s, ID:(%s)' % (name, os.getppid()))

# if __name__=='__main__':
#     print('Created one child process in windows Test:\n')
#     print('Current process is ID(%s)' % os.getpid())    # KEY: get current process ID: os.getpid()
#     # KEY: created child process
#     p = Process(target=newProcessProc, args=('ChildProcessName_XXX',)) # KEY: the input param for args is the input parameter of Proc
#     print('Child Process will start')
#     p.start()   # start child process
#     p.join()    # child process end
#     print('Child Process end.')


## Created process pool
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task name:%s, ID(%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('%s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('\n\nCreated process pool Test:\n')
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)                 # KEY: create a pool of process
#     for i in range(5):          # KEY: apply jobs to all process       
#         p.apply_async(long_time_task, args=('Task' + str(i),))
#     print('Waiting for all subprocesses done...')
#     p.close()                   # KEY: need to be called before join. Cannot add new process after p.close()
#     p.join()                    # KEY: wait for all process end
#     print('All subprocesses done.') 
#     # KEY: the max number of process working together is the number of core
#     #      CPU的核数，决定了可以有多少个process同时工作，其他process需要等待，直到有空闲的process出现，才可以开始

# # # # Reference
# # # print('range(1, 5) is:', list(range(1, 5)))
# # # print('range(5) is:', list(range(5)))

## 启动一个子进程，然后控制其输入和输出。
# import subprocess

# print('Equal to: \'$ nslookup www.python.org\'')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

## 进程间通信
from multiprocessing import Queue, Process
import os, time, random

def writeToQ(q):
    print('Write Process Start!')
    for ch in ['A', 'B', 'C', 'D']:
        print('Put %s into the Queue' % ch)
        q.put(ch)
        time.sleep(random.random()) # KEY: process to sleep and generated random number
    pass

def ReadFromQ(q):
    print('Read Process Start!')
    while True:
        value = q.get(True)
        print('%s is get from Queue' % value)
    pass

if __name__=='__main__':
    # KEY: Created a new Queue shared by different process. Pass in to Proc by agrs
    q = Queue() 
    # Define process
    processWriter = Process(target = writeToQ, args = (q,))
    processReader = Process(target = ReadFromQ, args = (q,))
    # Start process
    processWriter.start()
    processReader.start()
    # Wait for writer to stop, should stop before reader
    processWriter.join()
    # force reader to terminate. It: not a good way to do it
    processReader.terminate()

# # # # Result:
# # # Write Process Start!
# # # Put A into the Queue
# # # Read Process Start!
# # # A is get from Queue
# # # Put B into the Queue
# # # B is get from Queue
# # # Put C into the Queue
# # # C is get from Queue
# # # Put D into the Queue
# # # D is get from Queue
# # # Press any key to continue . . .








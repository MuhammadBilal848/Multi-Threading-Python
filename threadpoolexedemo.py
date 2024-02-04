import threading
import time
from concurrent.futures import ThreadPoolExecutor

def worker(n):
    print('Worker Starting Time(s)' , 0 )
    time.sleep(n)
    print('End Worker Time(s)' , n )
    return f'Total Time Taken(s) by Worker: {n}'

# The ThreadPoolExecutor class is a high-level interface for asynchronously executing callables.
# we can also control the number of threads that can run at the same time using ThreadPoolExecutor.
# ThreadPoolExecutor is a class in the concurrent.futures module that allows us to run threads in parallel.

def threadpooldemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(worker, 5)
        print(future1.result())
        future2 = executor.submit(worker, 3)
        print(future2.result())
        # here one thread will start and complete its cycle and then the second thread will start

threadpooldemo()

def threadpooldemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(worker, 5)
        future2 = executor.submit(worker, 3)
        print(future1.result())
        print(future2.result())
        # here both thearads will start at the same time and complete their respective cycle

threadpooldemo()
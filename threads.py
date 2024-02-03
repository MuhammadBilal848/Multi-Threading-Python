import threading
import time

def worker(n):
    print('Worker Starting Time(s)' , 0 )
    time.sleep(n)
    print('End Worker Time(s)' , n )

# s = time.time()
# worker(5)
# worker(3)
# e = time.time()
# print('Time Taken(s):', e-s)    

# we know that the worker function takes 5 seconds to complete, 
# so we can use threading to run the worker function in parallel.

s = time.time()
w1 = threading.Thread(target=worker, args=(5,))
w2 = threading.Thread(target=worker, args=(3,))

w1.start()
w2.start()

e = time.time()
print('Time Taken(s):', e-s)
import threading
import time

def worker(n):
    print('Worker Starting Time(s)' , 0 )
    time.sleep(n)
    print('End Worker Time(s)' , n )

s = time.time()
worker(5)
worker(3)
e = time.time()
print('Time Taken(s):', e-s)    

# we know that the worker function takes 5 seconds to complete, 
# so we can use threading to run the worker function in parallel.

s = time.time()
w1 = threading.Thread(target=worker, args=(5,))
w2 = threading.Thread(target=worker, args=(3,))

w1.start()
w2.start()

e = time.time()
print('Time Taken(s):', e-s)

# we can see that the time taken in the output is 0 seconds. But the worker function takes 5 seconds to complete.
# This is because the main thread is not waiting for the worker threads to complete.

# To fix this, we can use the join method to wait for the worker threads to complete.
s = time.time()
w1 = threading.Thread(target=worker, args=(5,))
w2 = threading.Thread(target=worker, args=(3,))

w1.start()
w2.start()

w1.join() # main thread will wait for w1 to complete
w2.join() # main thread will wait for w2 to complete

e = time.time()
print('Time Taken(s):', e-s)

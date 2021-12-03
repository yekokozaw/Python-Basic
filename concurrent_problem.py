from threading import *
import time

counter = 0
lock = Lock()
def increment():
    global counter

    for i in range(0,20000):
        lock.acquire()
        counter += 1
        lock.release()
def decrement():
    global counter
    
    for i in range(0,20000):
        lock.acquire()
        counter -= 1
        lock.release()

thread1 = Thread(target=increment)
thread2 = Thread(target=decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Counter ",counter)
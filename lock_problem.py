from threading import *
import time

lock = Lock()
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial ",factorial(3))


#dead lock
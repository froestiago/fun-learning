import time
import resource
import numpy as np

def bruteSumOfTwo(a, b, v):
    for i in a:
        for j in b:
            if i+j == v:
                return True
    return False

def sumOfTwo(a, b, v):
    x = {}
    for i in range(len(a)):
        difference = v - a[i]
        x[difference] = i
    
    for j in b:
        if j in x:
            return True
    return False

a = np.arange(0, 100000)
b = np.arange(0, 100000)


time_start = time.perf_counter()
print(bruteSumOfTwo(a, b, 199998))
time_elapsed = (time.perf_counter() - time_start)
print ("Brute Force\n\t%5.12f secs" % time_elapsed)


time_start = time.perf_counter()
print(sumOfTwo(a, b, 199998))
time_elapsed = (time.perf_counter() - time_start)
print ("Using Hash\n\t%5.12f secs" % time_elapsed)
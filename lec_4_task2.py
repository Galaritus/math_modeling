import numpy as np 
n = int(input())
a = np.zeros(n)
for i in range (0, n):
    a[i] = int(input())
b = np.array(a)
def muit_func(b):
    x = 1
    for i in range(len(b)):
        x *= b[i]
    return x 
print(muit_func(b))


    
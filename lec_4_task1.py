import numpy as np 
n = int(input())
a = np.zeros(n)
for i in range (0, n):
    a[i] = int(input())
b = np.array(a)
def mult_func(b):
        x = sum(b) / n
        return x
print(mult_func(b))
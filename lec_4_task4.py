import numpy as np
a = int(input())
b = int(input())
n = int(input())
y = 1
def mult_func(y):
    y1 = np.array(n)
    for i in np.linspace(a, b, n):
        y = i+1
        y1=np.append(y1, y)
    return y1
print(mult_func(y))
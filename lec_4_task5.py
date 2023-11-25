from math import *
a = input()
b = 0
c = 0
Sp = 0
St = 0
def mult_func(b):
    if a == 'круг':
        R = int(input())
        c = pi * R ** 2
        return c
    elif a == 'прямоугольник':
        a1 = int(input())
        b1 = int(input())
        Sp = a1 * b1
        return Sp
    elif a == 'треугольник':
        a1 = int(input())
        h = int(input())
        St = a1 * h * 0.5
        return St
print(mult_func(b))



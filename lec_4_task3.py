from lec_4_const import gravity_constant
h = int(input())
v = int(input())
m = int(input())
a = 0
def mult_func(a):
    a = (m * gravity_constant * h) + ((m * v ** 2) / 2)
    return a
print(mult_func(a))
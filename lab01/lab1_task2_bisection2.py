def f(x):
	import math
	return 0.1 * x**2 - x * math.log(x)


a = 1
b = 2
eps = 1e-5


while abs(b - a) > eps:

    x = (a + b) / 2
    
    if f(a) * f(x) < 0: b = x
   
    else: a = x

x = (a + b) / 2
print(x)

a = 2
b = 2
c = 2	
D = b**2 - 4*a*c
print(D)
x1 = (-b + D**0.5) / (2 * a)
x2 = (-b - D**0.5) / (2 * a)
x3 = (-b / (2 * a))
st1 = 'НЕТ КОРНЕЙ'
st2 = 'КОРНИ:'
st3 = 'КОРЕНЬ:'
if D > 0:
	print (st2)
	print (x1)
	print (x2)
elif D == 0:
	print(st3)
	print(x3)
else:
	 print (st1) 
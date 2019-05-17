import random
n = 10
l = [random.randint(0, 9) for _ in range(n)]
a = 3
b = 7
print(l)
for i in range(a, int((a + b) / 2)):
	j = b + a - i
	l[i], l[j] = l[j], l[i]
print(l)
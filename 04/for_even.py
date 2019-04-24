a = 0
b = 11
step = 2
# for i in range(a, b+1):
# 	if i % 2 == 0:
# 		print(i)

# for i in range(a, b+1, step):
# 	if a % 2 == 0:
# 		print(i)
# 	elif i != b:
# 		print(i + 1)

for i in range(a + a % 2, b + 1, step):
	print(i)
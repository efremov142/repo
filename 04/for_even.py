a = 20
b = 50
step = 10
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
# n = int(input('Enter n: '))
# n += 1 - n % 2
# for i in range(n):
# 	for j in range(n):
# 		if i > j:
# 			print('*', end='')
# 		else: print(' ', end='')
# 	print()

n=int(input("enter the no of rows :"))
for i in range(0,n+1):
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
if i==n:
    for i in range(n-1,0,-1):
        for j in range(0,n-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print()
	

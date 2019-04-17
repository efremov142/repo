import random
import math
fr = 1
to = 100
dollar = int(math.log(to-fr, 2))
num = random.randint(fr, to)
pnum = -1
while pnum != num:
	print('YOU HAVE %d DOLLARS' % dollar)
	pnum = int(input('guess a number from %d to %d: ' % (fr, to)))
	if pnum > num:
		print('your num is bigger')
	elif pnum < num:
		print('your num is smaller')
	else: 
		print('YOU WIN')
	dollar = dollar - 1 if dollar > 0 else 0

acc1 = 100000
acc2 = 100000
pers1 = 1.1
pers2 = 1.0
months = 24
gain1 = acc1 / 100 * pers1

i = 0
while i < months: 
# for i in range(months):
	num_of_month = i + 1
	acc1 += gain1
	gain2 = acc2 / 100 * pers2
	acc2 += gain2
	print('Month = %d\tacc1 = %.3f\tacc2 = %.3f' %\
		(num_of_month, acc1, acc2))
	if num_of_month % 12 == 0:
		if acc1 > acc2:
			print('Frist account is bigger')
		else:
			print('Second account is bigger')
	i += 1
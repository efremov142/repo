import msvcrt as m
while True:
	if m.getch().decode('utf-8') == '1':
		print('\r<', end='')
	else:
		print('\r>', end='')
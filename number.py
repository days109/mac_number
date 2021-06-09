a = int(input('choose the start number:'))
b = int(input('choode the end number:'))
import random
r = random.randint(a, b)
time = 0
while True:
	time = time + 1
	num = int(input('please fill in the number:'))
	if num == r:
		print('correct!')
		print('you have tried', time, 'time')
		break
	elif num > r:
		print('smaller')
	else:
		print('bigger')

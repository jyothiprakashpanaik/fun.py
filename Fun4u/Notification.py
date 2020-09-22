import time
from playsound import playsound 

while True:
	if (time.localtime()[3] < 9 or time.localtime()[3] > 17):
		break;

	print('Brink water')
	time.sleep(30*60)

	print('eye exersise')
	time.sleep(45*60)

	print('exersise')


	

	
import random
import time

def perebor(text,speed=0.05):
	'''speed: slow=0.05, norm=0.025,fast=0.01'''
	index = len(text)-1
	t = 1
	for i in text:
		while True:
			a = chr(random.randint(32,126))
			if t == 1:
				print(a,end='\r')
			elif t == index:
				break
			else:
				print(text[:t],a,sep='',end='\r')
			time.sleep(speed)
			if a == i:
				t += 1
				break
	print(text)

# speed = input()
# speed = float(speed)

perebor("Hello world!",0.01)
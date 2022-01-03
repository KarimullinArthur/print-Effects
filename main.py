import random
import time

def perebor(text,speed=0.05,mode='standard'):
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

text = input("Input text: ")

speed = input("\nRecomend\nslow=0.025\nnorm=0.01\nfast=0.001\nInput speed(s): ")
speed = float(speed)

perebor(text,speed,'save')

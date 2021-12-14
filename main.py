import random
import time
letters = ['h','e','l','o','w','r','d',' ']

text = 'hello world'
index = len(text)-1
b = index-1
s = " "
for i in text:
    while True:
        a = letters[random.randint(0,len(letters)-1)]
        print(a,end='\r')
        time.sleep(0.1)
        if a == i:
            print(text[:index-b],end='')
            b -= 1
            s += " "
            break   

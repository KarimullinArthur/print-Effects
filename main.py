import random
import time
letters = ['h','e','l','o','w','r','d',' ']

text = 'hello world'
index = len(text)-1
t = 1
for i in text:
    while True:
        a = letters[random.randint(0,len(letters)-1)]
        print(text[:t],a,sep='',end='\r')
        time.sleep(0.1)
        if a == i:
            t += t
            break

print(text)

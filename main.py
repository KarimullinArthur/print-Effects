import random
import time

text = input()
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
        time.sleep(0.05)
        if a == i:
            t += 1
            break

print(text)

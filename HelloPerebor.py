import random
import time
letters = ['h','e','l','o','w','r','d',' ']

text = 'hello world'
index = len(text)-1
for i in text:
    while True:
        a = letters[random.randint(0,len(letters)-1)]
        print(a,end='\r')
        time.sleep(0.1)
        if a == i:
            print(i)
#            b = index-1
#            print(text[:],end='')
#            b += 1
#            print('OK')
            break   

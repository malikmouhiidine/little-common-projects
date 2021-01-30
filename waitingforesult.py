from random import randint
import time

head=0

for i in range(1, 301):
    if randint(0, 1)==1:
        head+=1
    if i == 100:
        print('waiting for results', end='', flush=True)
        for _ in range(1, 11):
            print('. ', end='', flush=True)
            time.sleep(.4)
        print()

time.sleep(2.4)
print('you got head '+ str(head) +' times')
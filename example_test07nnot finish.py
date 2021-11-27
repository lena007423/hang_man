from time import sleep
time = int(input("enter time:"))
from time import sleep

def number():
    n = 0 
    while True :
        n += 1
        time -= 1
        sleep(1)
        print(n)
        if time == 0:
            n == -1
            break
number()
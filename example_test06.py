from time import sleep

def number():
    n = 0 
    while True  :
        n += 1
        sleep(1)
        if n % 7 == 0:
            print("hop")
        else:
            print(n)
number()
from time import sleep
number = int(input("enter a number"))

def co(number):
    while number :
        number -= 1
        sleep(1)
        print(number)
co(number)
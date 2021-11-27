from time import sleep 
for i in range(101):
    sleep(1)
    if i % 2 == 0:
        print(i)
        print ('even')
    else:
        print(i)
        print ("odd")
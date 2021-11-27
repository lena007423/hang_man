from time import sleep 

for E in range(100):
    sleep(0.1)
    print(E)

    if E % 11 == 0: 
        
        print ("Hop")
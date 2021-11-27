from time import sleep
Seconds = 0
Minutes = 0
Hours = 0
for i in range(1000000):
    sleep(1)
    print(Hours, ":", Minutes, ":", Seconds) 
    Seconds +=1
    if Seconds == 60:
        Seconds = 0
        Minutes += 1
    elif Minutes == 60:
        Minutes = 0
        Hours = 1

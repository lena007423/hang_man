name1 = ("Amir")
name2 = ("Aidin")
name3 = ("Mina")
names = [name1, name2, name3]
for i in names:
    for x in i:
        if x ==  "M":
        #if x == "m":
            names.remove(i)



print (names)
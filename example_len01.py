l1 = input("Enter a name : ")
l2 = input("Enter a name : ")
l3 = input("Enter a name : ")
l4 = input("Enter a name : ")
l5 = input("Enter a name : ")
names = [l1, l2, l3, l4, l5]
for i in names:
    if len(i) >= 7:
        names.remove(i)
print(names)
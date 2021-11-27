l1 = int(input("enter number : "))
l2 = int(input("enter number : "))
l3 = int(input("enter number : "))
l4 = int(input("enter number : "))
l5 = int(input("enter number : "))
numers = [l1, l2, l3, l4, l5]
for i in numers: 
    if int(i) % 2 != 0:
        numers.remove(i)
print(numers)
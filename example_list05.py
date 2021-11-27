l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
s = 3
while s > 0:
    input1 = input("enter name =")
    l1.append(input1)
    s -= 1
w = 3
while w > 0:
    input2 = input("enter name =")
    l2.append(input2)
    w -= 1
d = 3
while d > 0:
    input3 = input("enter name =")
    l3.append(input3)
    d -= 1
x = 3
while x > 0:
    input4 = input("enter name =")
    l4.append(input4)
    x -= 1
c = 3
while c > 0:
    input5 = input("enter name =")
    l5.append(input5)
    c -= 1
l1.extend(l2)
l1.extend(l3)
l1.extend(l4)
l1.extend(l5)
print(l1)
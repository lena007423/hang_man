
num  = int(input("how many numbers do you want to compare? "))

list_number = list()

for i in range(0,num):
    inp_num = int(input("please enter a number"))
    list_number.append(inp_num)

for x in range(0, len(list_number)):
    for y in range(x, len(list_number)):
        if list_number[x]>list_number[y]:
            a_con = list_number[y]
            list_number[y] = list_number[x]
            list_number[x] =a_con

print(list_number)
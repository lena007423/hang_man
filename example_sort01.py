num = int(input("how many numbers : "))
list_numer = list()
for i in range(0, num):
    inp_num = int(input('enter number'))
    list_numer.append(inp_num)
list_numer.sort()
print(list_numer)
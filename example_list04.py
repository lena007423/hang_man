animal_list = ["cat", "dog"]
s = 5
while s > 0:
    l = len(animal_list)
    input1 = input("enter a word")
    animal_list.append(input1)
    s -= 1
print(animal_list)
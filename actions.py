import random 
from data import * 
def random_word():
    index = random.randint(0, len(words)-1)
    return words[index]
def final_alphabet(alphabet, word, list1):
    for i in range(0, len(word)):
        if word[i] == alphabet:
            list1[i] = alphabet
    return list1
def join_alphabet(list1):
    gussed_word = " ".join(list1)
    return gussed_word


    
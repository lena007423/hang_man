from typing import final
from actions import *
out1 = random_word()
print (out1)
out2 = len(out1)*["-"]
out3 = join_alphabet(out2)
print(out3)
failed_counter = 0

while failed_counter < 7 :
    gussed_letter = (input("enter a letter : "))
    result_list = final_alphabet(gussed_letter, out1, out2)
    result_word = join_alphabet(result_list)
    print(result_word)
    if failed_counter == 6:
        print("YOU ARE LOSER")
        break
    elif not gussed_letter in out1:
        failed_counter += 1
        print (HANGMANPICS[failed_counter])
    elif not "-" in result_word :
        print("you are winner")
        break 
    
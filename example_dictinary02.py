dic_morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "p":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
}


input_word = input('please enter your word: ')
translate = ''
for character in input_word:

    translate = translate + dic_morse[character.upper()]

print(translate) 
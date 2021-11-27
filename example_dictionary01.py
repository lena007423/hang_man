phone_numbers = {
    "MA" : "09188666511",
    "DA" : "0912 5959023",
    "GM" : "09188666511",
    "AUZ" : "09126582812",
    "AUSH" : "09183664854",
    "GF" : "09183656319"
}
action = (input("Enter Delete, Update or Add or Read: "))
def editor(action):
    if action == "Delete":
        person_name = input("Enter a name: ")
        phone_numbers.pop(person_name)
        print(phone_numbers)
    elif action == "Read":
        person_name = input("Enter a name: ")
        print(phone_numbers[person_name])
    elif action == "Add" or "Update": 
        person_name = input("Enter a name: ")
        numbers = input("Enter number : ")
        phone_numbers.update({person_name : numbers})
        print(phone_numbers)

editor(action)

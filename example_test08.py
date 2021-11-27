list_of_duties = list()
def to_do_list():
    while True:
        input_duty = input("enter you works:")
        if input_duty == 'stop':
            print(list_of_duties)
            break
        list_of_duties.append(input_duty)
to_do_list()

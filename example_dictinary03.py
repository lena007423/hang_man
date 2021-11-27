dic = {
    "trosers" :{
       "36":['gray', "orang", "green"],
       "38":["green", "black"],
       "40":["black", "pink", "purple"],
    },
    "scarf" : ["orange", "black", "white"],
    "skirt" :{
        "long" : ["black"],
        "short" : ["black", "pink"]
    }
}
color = (input("what color do you whant? "))
def get_input (ac_list):
    print("product", ac_list)
    ap = input("wich product do you mean? ")
    while not ac_list.__contains__(ac):
        ap = input("wich product do you mean? ")
    else:
        print(category, dic(ap).keys())
        ac = input("wich category do you mean? ")

        if color in (dic[ap][ac]) :
            print("yes")
        else :
            print("No")
get_input ("trosers", "scarf", "skirt")
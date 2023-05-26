import time

r = ["Y", "y", "Yes", "yes"]
g = ["N", "No", "n", "no"]
zubat = ["Zubat", "zubat"]
gastly = ["Gastly", "gastly"]
pokeball = ["Pokeball", "pokeball"]
greatball = ["Greatball", "greatball"]
x = True
inventory = []

def Cave_Option():
    time.sleep(1.5)
    print("-------\nYou enter the dark and gloomy cave.")
    time.sleep(1.5)
    print("As you turn a corner, you encounter a wild Zubat and Gastly")
    user_request3 = input("Do you want to attempt at catching one? Y/N: ")
    if user_request3 in r:
        choice1 = input("which one do you want to catch? ")
        print(choice1)
        if choice1 in zubat:
            from Zubat import Zubat_Option
            print(Zubat_Option)
        else:
            return Cave_Option()
    if user_request3 in g:
        choice2 = input("Return to pond? Y/N: ")
        if choice2 in r:
            from Pond import Pond_Option
            print(Pond_Option)
        else:
            return Cave_Option()
    else:
        x = True
        while x == True:
            q = input("Looks like something went wrong. Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Cave_Option()
print(Cave_Option())

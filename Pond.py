import time

r = ["Y", "y", "Yes", "yes"]
g = ["N", "No", "n", "no"]
squirtle = ["Squirtle", "squirtle"]
psyduck = ["Psyduck", "psyduck"]
pokeball = ["Pokeball", "pokeball"]
x = True
inventory = []

def Pond_Option():
    time.sleep(1.5)
    print("As you walk closer, you come across a wild Squirtle and Psyduck.")
    user_request3 = input("Do you want to attempt at catching one? Y/N: ")
    if user_request3 in r:
        choice1 = input("Which one do you want to catch? ")
        print(choice1)
        if choice1 in squirtle:
            from Squirtle import Squirtle_Option
            print(Squirtle_Option)

        else:
            return Pond_Option()
    if user_request3 in g:
        choice2 = input("Return to Cave? Y/N: ")
        if choice2 in r:
            from Cave import Cave_Option
            print(Cave_Option)
        else:
            return Pond_Option()
    else:
        x = True    
        while x == True:
            q = input("Looks like something went wrong. Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Pond_Option()
print(Pond_Option())

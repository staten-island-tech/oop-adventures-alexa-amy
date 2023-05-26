import time

r = ["Y", "y", "Yes", "yes"]
g = ["N", "No", "n", "no"]
squirtle = ["Squirtle", "squirtle"]
psyduck = ["Psyduck", "psyduck"]
pokeball = ["Pokeball", "pokeball"]
greatball = ["Greatball", "greatball"]
cave_return = ["Cave", "cave"]
x = True
from storyline import inventory

def Psyduck_Option():
    pokeball_request = input("Pick a pokeball - Pokeball or Greatball: ")
    if pokeball_request in pokeball:
        print("-------\nYou now have 14x Pokeballs remaining")
        print("-------\nYou throw your Pokeball at Psyduck, but miss.")
    if pokeball_request in greatball:
        print("------\nYou now have 4x Greatballs remaining")
        print("-------\nYou throw your Greatball at Psyduck, but miss.")
    else:   
        while x == True:
            q = input("Looks like something went wrong. Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                break

    user_request5 = input("Do you wish to catch Psyduck again? Y/N: ")
    if user_request5 in r:
        user_request6 = input("Pick your Pokeball - Pokeball or Greatball: ")
        if user_request6 in pokeball:
            print("-------\nYou now have 13x Pokeballs remaining")
            print("-------\nYou throw your Pokeball at Psyduck..")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("You have successfully captured Psyduck!")
            inventory.append("Psyduck")
        if user_request6 in greatball:
            print("------\nYou now have 3x Greatballs remaining")
            print("You throw your Greatball at Psyduck..")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("You have successfully captured Psyduck!")
            inventory.append("Psyduck")
    
    if user_request5 in g:
        choice2 = input("Want to catch Squirtle instead or go to the Cave?\nType 'Squirtle' for Squirtle or 'Cave' for Cave: ")
        if choice2 in squirtle:
            from Squirtle import Squirtle_Option
            print(Squirtle_Option)
        else:
            return Psyduck_Option
        if choice2 in cave_return:
            from Cave import Cave_Option
            print(Cave_Option)
        else:
            return Psyduck_Option()
print(Psyduck_Option())
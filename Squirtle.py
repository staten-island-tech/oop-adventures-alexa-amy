import time

r = ["Y", "y", "Yes", "yes"]
g = ["N", "No", "n", "no"]
squirtle = ["Squirtle", "squirtle"]
psyduck = ["Psyduck", "psyduck"]
pokeball = ["Pokeball", "pokeball"]
greatball = ["Greatball", "greatball"]
cave_return = ["Cave", "cave"]
inventory = []
x = True
y = True

def Squirtle():
    pokeball_request = input("Pick a pokeball - Pokeball or Greatball: ")
    if pokeball_request in pokeball:
        print("-------\nYou now have 14x Pokeballs remaining")
        print("-------\nYou throw your Pokeball at Squirtle, but miss.")
    elif pokeball_request in greatball:
        print("------\nYou now have 4x Greatballs remaining")
        print("You throw your Greatball at Squirtle, but miss.")
    else:   
        while x == True:
            q = input("Looks like something went wrong. Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                break
    
    user_request5 = input("Do you wish to catch Squirtle again? Y/N: ")
    if user_request5 in r:
        user_request6 = input("Pick your Pokeball - Pokeball or Greatball: ")
        if user_request6 in pokeball:
            print("-------\nYou now have 13x Pokeballs remaining")
            print("-------\nYou throw your Pokeball at Squirtle..")
        if user_request6 in greatball:
            print("------\nYou now have 3x Greatballs remaining")
            print("You throw your Greatball at Squirtle..")

    if user_request5 in g:
        choice2 = input("Want to catch psyduck instead or go to the cave?\nType 'Psyduck' for Psyduck or 'Cave' for Cave: ")
        if choice2 in psyduck:
            from Psyduck import Psyduck_Option
        else:
            print("Returning to Squirtle..")
            return Squirtle()
        if choice2 in cave_return:
            from Cave import Cave_Option
        else:
            print("Returning to Squirtle..")
            return Squirtle()
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("You have successfully captured Squirtle!")
    inventory.append("Squirtle")
Squirtle()
import time

r = ["Y", "y", "Yes", "yes"]
g = ["N", "No", "n", "no"]
squirtle = ["Squirtle", "squirtle"]
psyduck = ["Psyduck", "psyduck"]
pokeball = ["Pokeball", "pokeball"]
greatball = ["Greatball", "greatball"]
cave_return = ["Cave", "cave"]
x = True
inventory = []

def Squirtle():
    pokeball_request = input("Pick a pokeball: Pokeball or Greatball: ")
    if pokeball_request in pokeball:
        print("-------\nYou now have 14x Pokeballs remaining")
        print("-------\nYou throw your Pokeball at Squirtle, but miss.")
    if pokeball_request in greatball:
        print("------\nYou now have 4x Greatballs remaining")
        print("You throw your Greatball at Squirtle, but miss.")
    else:   
        while x == True:
            q = input("Looks like something went wrong. Would you like to continue? Y/N: ")
            if (q== "N" or q== "No" or q=="n" or q=="no"):
                x = False
                break
    user_request5 = input("Do you wish to try again? Y/N: ")
    if user_request5 in r:
        user_request6 = input("Pick your Pokeball: ")
        if user_request6 in pokeball:
            print("-------\nYou now have 13x Pokeballs remaining")
        else:
            print("------\nYou now have 3x Greatballs remaining")
    if user_request5 in g:
        choice2 = input("Want to catch psyduck instead or go to the cave?\nType 'Psyduck' for Psyduck or 'Cave' for Cave: ")
        if choice2 in psyduck:
            from Psyduck import Psyduck
        else:
            return Squirtle()
        if choice2 in cave_return:
            from Cave import Cave
        else:
            return Squirtle()
    
    #did not fix yet
    else:
        user_request4 = input("Which one do you want to catch? ")    
    print("You throw your",user_request6, "at Squirtle..")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("You have successfully captured Squirtle!")
    inventory.append("Squirtle")
Squirtle()
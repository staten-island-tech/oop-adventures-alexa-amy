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

def Psyduck_Option():
    pokeball_request = input("Pick a pokeball: Pokeball or Greatball: ")
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
    
    #did not fix yet
    user_request5 = input("Do you wish to try again? Y/N: ")
    if user_request5 in r:
        user_request6 = input("Pick your Pokeball: ")
        if user_request6 in pokeball:
            print("-------\nYou now have 13x Pokeballs remaining")
            print("You throw your Pokeball at Psyduck..")
        else:
            print("------\nYou now have 3x Greatballs remaining")
            print("You throw your Greatball at Psyduck..")
        time.sleep(1.5)
        print("...")
        time.sleep(1.5)
        print("You have successfully captured Psyduck!")
        inventory.append("Psyduck")
Psyduck_Option()
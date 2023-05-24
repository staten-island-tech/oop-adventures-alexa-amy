import time
a = 1
b = 1.5
c = 2

r = ["Y", "y", "Yes", "yes"]
g = ["N", "n", "No", "no"]
squirtle = ["Squirtle", "squirtle"]
psyduck = ["Psyduck", "psyduck"]
pokeball = ["Pokeball", "pokeball"]
greatball = ["Greatball", "greatball"]
x = True

def Pond():
    print("-------\nAs you walk around the forest, you see a pond nearby.")
    time.sleep(b)
    print("As you walk closer, you come across a wild Squirtle and Psyduck.")
    user_request3 = input("Do you want to attempt at catching one? Y/N: ")
    if user_request3 in r:
        user_request4 = input("Which one do you want to catch? ")
        if user_request4 in squirtle:
            pokeball_request = input("Pick a pokeball: Pokeball or Greatball: ")
            if pokeball_request in pokeball:
                print("-------\nYou now have 14x Pokeballs remaining")
            else:
                print("------\nYou now have 4x Greatballs remaining")
            print("You throw your",pokeball_request, "at Squirtle, but miss.")
            user_request5 = input("Do you wish to try again? Y/N: ")
            if user_request5 in r:
                user_request6 = input("Pick your Pokeball: ")
            if user_request6 in pokeball:
                print("-------\nYou now have 13x Pokeballs remaining")
            else:
                print("------\nYou now have 3x Greatballs remaining")
            print("You throw your",user_request6, "at Squirtle..")
            time.sleep(b)
            print("...")
            time.sleep(b)
            print("You have successfully captured Squirtle!")
            #
            print("")
        else:
            if user_request4 in psyduck:
                pokeball_request = input("Pick a pokeball: Pokeball or Greatball: ")
                if pokeball_request in pokeball:
                    print("-------\nYou now have 14x Pokeballs remaining")
                else:
                    print("------\nYou now have 4x Greatballs remaining")
                print("You throw your",pokeball_request, "at Psyduck, but miss.")
                user_request5 = input("Do you wish to try again? Y/N: ")
                if user_request5 in r:
                    user_request6 = input("Pick your Pokeball: ")
                if user_request6 in pokeball:
                    print("-------\nYou now have 13x Pokeballs remaining")
                else:
                    print("------\nYou now have 3x Greatballs remaining")
                print("You throw your",user_request6, "at Psyduck..")
                time.sleep(b)
                print("...")
                time.sleep(b)
                print("You have successfully captured Psyduck!")
    else:
        while x == True:
            q = input("It seems you made a mistake. Please try again: ")
            if q in r:
                x = False
Pond()
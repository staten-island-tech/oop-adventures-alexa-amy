# You are a student in Mr. Whalen's pokemon training center. 
# In order to graduate you must beat him in a pokemon battle.
# However you don't have any pokemon to begin with.
# Go into the forest to search for some pokemon.

# Here is a gift to help you:
# 15x Pokeball, 5x Greatball, and 5x Sitrus Berry!

# Good luck on your journey!

# ------

# Would you like to enter the forest? Y/N
# Y: You enter the forest, wild pokemon surround the area..
# N: 
# You look around your area and notice there is a pond ahead, and a cave.
# Would you like to go to the pond or the cave?
# Pond: You come across a wild Squirtle and Psyduck.
    # Do you want to attempt at catching one? Y/N
    # N: You run away from the area and go into the cave instead.
    # Y: Which one do you want to catch?
        # Pick your pokeball: 
            # You now have 4x Greatball
            # You now have 14x Pokeball
    # Squirtle: You throw your {pokeball} at Squirtle, but miss.
    # Squirtle: Do you wish to try again? Y/N
        # Y: Pick your pokeball:
        # You now have 3x Greatball
        # You now have 13x Pokeball
    # Squirtle: You throw your {pokeball} at Squirtle and successfully catch it!
    # Squirtle: Would you like to name it?

import time
""" 
x = True
while x == True:
    print("-------\nYou are a student in Mr. Whalen's pokemon training center.\nIn order to graduate you must beat him in a pokemon battle.\nHowever you don't have any pokemon to begin with.\nGo into the forest to search for some pokemon.")
    print("-------\nHere is a gift to help you: \n15x Pokeball, 5x Greatball, and 5x Sitrus Berry!\nGood luck on your journey!")
    Forest_Request = input("-------\nWould you like to enter Flourish Forest? Y/N: ")
    if Forest_Request == "Y" or "Yes":
        print("-------\nYou enter the Flourish Forest and see many wild pokemon surrounding the area..")
    else:
        print("You must enter because I said so")
        still_continue = input("Would you like to continue? Y/N: ")
        Forest_Request = still_continue
    print("You look around the area and notice there is a pond ahead, and a cave.")
    user_request2 = input("Would you like to go to the pond or the cave? " )
    if user_request2 == "Pond" or "pond":
        print("-------\nYou come across a wild Squirtle and Psyduck.")
        user_request3 = input("Do you want to attempt at catching one? Y/N: ")
        if user_request3 == "Y" or "Yes":
            user_request4 = input("Which one do you want to catch? ")
            if user_request4 == "Squirtle" or "squirtle":
                pokeball_request = input("Pick a pokeball: Pokeball or Greatball: ")
                if pokeball_request == "Pokeball":
                    print("-------\nYou now have 14x Pokeballs remaining")
                else:
                    print("------\nYou now have 4x Greatballs remaining")
                print("You throw your", {pokeball_request}, "at Squirtle, but miss.")
    user_request5 = input("Do you wish to try again? Y/N: ")
    if user_request5 == "Y" or "Yes":
        user_request6 = input("Pick your Pokeball: ")
        if pokeball_request == "Pokeball":
            print("-------\nYou now have 13x Pokeballs remaining")
        else:
            print("------\nYou now have 3x Greatballs remaining")

    q = input("Would you like to continue? Y/N: ")
    if (q== "Y" or q== "Yes"):
        x = False
        break """

print("-------\nYou are a student in Mr. Whalen's pokemon training center.")
time.sleep(2)
print("In order to graduate you must beat him in a pokemon battle.")
time.sleep(2)
print("However you don't have any pokemon to begin with.")
time.sleep(2)
print("Go into the forest to search for some pokemon.")
time.sleep(2)
print("-------\nHere is a gift to help you:")
time.sleep(1.5)
print("15x Pokeball, 5x Greatball, and 5x Sitrus Berry!")
time.sleep(2)
print("Good luck on your journey!")
time.sleep(2)

r = ["Y", "y", "Yes", "yes"]
Forest_Request = input("-------\nWould you like to enter Flourish Forest? Y/N: ")
if Forest_Request in r:
    time.sleep(1)
    print("-------\nYou enter the Flourish Forest and see many wild pokemon surrounding the area..")
    time.sleep(2)
    print("You look around the area and notice there is a pond ahead, and a cave.")
    user_request2 = input("Would you like to go to the pond or the cave? " )
    if user_request2 == "Pond" or "pond":
        print("-------\nYou come across a wild Squirtle and Psyduck.")
        user_request3 = input("Do you want to attempt at catching one? Y/N: ")
    

if user_request3 == "Y" or "Yes":
        user_request4 = input("Which one do you want to catch? ")

if user_request4 == "Squirtle" or "squirtle":
    pokeball_request = input("Pick a pokeball: Pokeball or Greatball: ")
    if pokeball_request == "Pokeball":
        print("-------\nYou now have 14x Pokeballs remaining")
    else:
        print("------\nYou now have 4x Greatballs remaining")
        print("You throw your", {pokeball_request}, "at Squirtle, but miss.")
    user_request5 = input("Do you wish to try again? Y/N: ")
    if user_request5 == "Y" or "Yes":
        user_request6 = input("Pick your Pokeball: ")
        if pokeball_request == "Pokeball":
            print("-------\nYou now have 13x Pokeballs remaining")
        else:
            print("------\nYou now have 3x Greatballs remaining")
else:
    print("You must enter because I said so :)")
    continue1 = input("Would you like to continue? Y/N: ")
    Forest_Request = continue1
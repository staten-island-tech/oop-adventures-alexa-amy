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
    time.sleep(1.5)
    user_request2 = input("Would you like to go to the pond or the cave? " )
    time.sleep(1.5)
    from Pond import *
    Pond = Pond_Option()
else:
    print("You must enter because I said so :)")
    continue1 = input("Would you like to continue? Y/N: ")
    Forest_Request = continue1
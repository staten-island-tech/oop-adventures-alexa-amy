import time
a = 1
b = 1.5
c = 2

#import user then below
print("-------\nYou are a student in Mr. Whalen's pokemon training center.")
time.sleep(c)
print("In order to graduate you must beat him in a pokemon battle.")
time.sleep(c)
print("However you don't have any pokemon to begin with.")
time.sleep(c)
print("Go into the forest to search for some pokemon.")
time.sleep(c)
print("-------\nHere is a gift to help you:")
time.sleep(b)
print("15x Pokeball, 5x Greatball, and 5x Sitrus Berry!")
time.sleep(c)
print("Good luck on your journey!")
time.sleep(c)

r = ["Y", "y", "Yes", "yes"]
c = ["Cave", "cave"]
Forest_Request = input("-------\nWould you like to enter Eterna Forest? Y/N: ")
if Forest_Request in r:
    time.sleep(1)
    print("-------\nYou enter the Eterna Forest and see many wild pokemon surrounding the area..")
    time.sleep(2)
    print("You look around the area and notice there is a pond ahead, and a cave.")
    time.sleep(1.5)
    user_request2 = input("Would you like to go to the pond or the cave? ")
    if user_request2 in c:
        from Cave import Cave_Option
        from PokemonRefresh import Pokemon_Refresh
    else:
        from Pond import Pond_Option
        from PokemonRefresh import Pokemon_Refresh
else:
    print("You must enter because I said so :)")
    continue1 = input("Would you like to continue? Y/N: ")
    Forest_Request = continue1

import time
a = 1
b = 1.5
c = 2

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
Forest_Request = input("-------\nWould you like to enter Flourish Forest? Y/N: ")
if Forest_Request in r:
    time.sleep(a)
    print("-------\nYou enter the Flourish Forest and see many wild pokemon surrounding the area..")
    time.sleep(c)
    print("You look around the area and notice there is a pond ahead, and a cave.")
    time.sleep(b)
    user_request2 = input("Would you like to go to the pond or the cave? " )
    if user_request2 == "Cave" or "cave":
        from Cave import Cave
    else:
        from Pond import Pond
else:
    print("You must enter because I said so :)")
    continue1 = input("Would you like to continue? Y/N: ")
    Forest_Request = continue1

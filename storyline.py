import time
from classes import User

inventory = []
r = ["Y", "y", "Yes", "yes"]
c = ["Cave", "cave"]
p = ["Pond", "pond"]


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

def Forest_Start():
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
            print(Cave_Option)
        elif user_request2 in p:
            from Pond import Pond_Option
            print(Pond_Option)
        else:
            time.sleep(1.5)
            print("Sorry. Looks like something went wrong.\nReturning to Eterna Forest..")
            print(Forest_Start())
    else:
        print("You must enter because I said so :)")
        x = True    
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Forest_Start()
print(Forest_Start())
import time
import random

r = ["Y", "y", "Yes", "yes"]
squirtle = ["Squirtle", "squirtle"]
psyduck = ["Psyduck", "psyduck"]
zubat = ["Zubat", "zubat"]
gastly = ["Gastly", "gastly"]
feeding = ["Feed", "Feeding", "feed", "feeding",]
list1 = ["Your Pokemon was uncomfortable..", "Your Pokemon enjoyed that!"]
list2 = ["Stats: +100 defense", "Stats: +15 defense", "Stats: +20 attack", "Stats:"]
aff_points = 0
x = True

class Pokemon_Refresh():
    def __init__(self):
        print("Pokemon Refresh has been selected")
    print("-------\nWelcome to Pokemon Refresh!")
    time.sleep(2)
    print("There are five different ways to care for Pokémon:")
    time.sleep(2)
    print("Using a comb, a brush, a towel, a dryer, or feeding it.")
    time.sleep(2)
    print("Caring for a Pokémon increases its affection and stats.")
    time.sleep(2)
    while x == True:
        care_request = input("Which item would you like to use?: ")
        if care_request == "Comb" or "comb":
            print(random.choice(list1))
            if random.choice(list1) == "Your Pokemon was uncomfortable..":
                print("Stats: -10 in defense")
                aff_points = aff_points - 10
                print("Current number of affection points:",aff_points)
            else:
                print("Stats: +20 in attack")
                aff_points = aff_points + 20
                print("Current number of affection points:",aff_points)
        q = input("Would you like to continue? Y/N: ")
        if (q== "N" or q== "No"):
            x = False
            break
            

"""     if care_request == "Brush" or "brush":
        print(random.choice(list1))
        if list1[0]:
            print("Stats: -10 in attack")
        else:
            print("Stats: +50 in attack")
    if care_request == "Towel" or "towel":
        print(random.choice(list1))
        if list1[0]:
            print("Stats: -10 in defense")
        else:
            print("Stats: +15 in defense") """
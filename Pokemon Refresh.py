import time
import random

r = ["Y", "y", "Yes", "yes"]
squirtle = ["Squirtle", "squirtle"]
psyduck = ["Psyduck", "psyduck"]
zubat = ["Zubat", "zubat"]
gastly = ["Gastly", "gastly"]
feeding = ["Feed", "Feeding", "feed", "feeding",]
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
    care_request = input("Which item would you like to use?: ")
    if care_request == "Comb" or "comb":
        list1 = ["Your pokemon was uncomfortable..", "Your pokemon enjoyed that!"]
        print(random.choice(list1))
        if list1[0]:
            print("Stats -10 in defense")
        else:
            print("States +20 in attack")
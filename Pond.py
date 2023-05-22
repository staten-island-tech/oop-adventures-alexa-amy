r = ["Y", "y", "Yes", "yes"]
x = True
class Pond_Option:
    def __init__(self):
        print("")
    user_request2 = input("Would you like to go to the pond or the cave? " )
    while x == True:
        q = input("It seems you made a mistake. Please try again: ")
        if user_request2 == "Pond" or "pond":
            x = False
            break
        print("-------\nYou come across a wild Squirtle and Psyduck.")
    user_request3 = input("Do you want to attempt at catching one? Y/N: ")
    if user_request3 in r:
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
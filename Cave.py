import time
a = 1
b = 1.5
c = 2

r = ["Y", "y", "Yes", "yes"]
zubat = ["Zubat", "zubat"]
gastly = ["Gastly", "gastly"]
pokeball = ["Pokeball", "pokeball"]
x = True

class Cave_Option():
    def __init__(self):
        print("Cave has been selected")
    print("-------\nYou enter the dark and gloomy cave.")
    print("As you turn a corner, you encounter a wild Zubat and Gastly")
    user_request3 = input("Do you want to attempt at catching one? Y/N: ")
    if user_request3 in r:
        user_request4 = input("Which one do you want to catch? ")
        if user_request4 in zubat:
            pokeball_request = input("Pick a pokeball: Pokeball or Greatball: ")
            if pokeball_request in pokeball:
                print("-------\nYou now have 14x Pokeballs remaining")
            else:
                print("------\nYou now have 4x Greatballs remaining")
            print("You throw your",pokeball_request, "at Zubat, but miss.")
            user_request5 = input("Do you wish to try again? Y/N: ")
            if user_request5 in r:
                user_request6 = input("Pick your Pokeball: ")
            if user_request6 in pokeball:
                print("-------\nYou now have 13x Pokeballs remaining")
            else:
                print("------\nYou now have 3x Greatballs remaining")
            print("You throw your",user_request6, "at Zubat..")
            time.sleep(b)
            print("...")
            time.sleep(b)
            print("You have successfully captured Zubat!")
        else:
            if user_request4 in gastly:
                pokeball_request = input("Pick a pokeball: Pokeball or Greatball: ")
                if pokeball_request in pokeball:
                    print("-------\nYou now have 14x Pokeballs remaining")
                else:
                    print("------\nYou now have 4x Greatballs remaining")
                print("You throw your",pokeball_request, "at Gastly, but miss.")
                user_request5 = input("Do you wish to try again? Y/N: ")
                if user_request5 in r:
                    user_request6 = input("Pick your Pokeball: ")
                if user_request6 in pokeball:
                    print("-------\nYou now have 13x Pokeballs remaining")
                else:
                    print("------\nYou now have 3x Greatballs remaining")
                print("You throw your",user_request6, "at Gastly..")
                time.sleep(b)
                print("...")
                time.sleep(b)
                print("You have successfully captured Gastly!")
    else:
        while x == True:
            q = input("It seems you made a mistake. Please try again: ")
            if q in r:
                x = False
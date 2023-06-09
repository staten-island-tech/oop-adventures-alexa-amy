import time

r = ["Y", "y", "Yes", "yes"]
g = ["N", "No", "n", "no"]
zubat = ["Zubat", "zubat"]
gastly = ["Gastly", "gastly"]
pokeball = ["Pokeball", "pokeball"]
greatball = ["Greatball", "greatball"]
cave_return = ["Cave", "cave"]
pond_return = ["Pond", "pond"]
battle5 = ["Battle", "battle", "BATTLE", "b"]
gotoshop = ["Shop", "shop", "SHOP", "s"]
x = True

def Zubat_Option():
    pokeball_request = input("Pick a pokeball - Pokeball or Greatball: ")
    if pokeball_request in pokeball:
        print("-------\nYou now have 14x Pokeballs remaining")
        print("-------\nYou throw your Pokeball at Zubat, but miss.")
    elif pokeball_request in greatball:
        print("------\nYou now have 4x Greatballs remaining")
        print("-------\nYou throw your Greatball at Zubat, but miss.")
    else:
        while x == True:
            q = input("Looks like something went wrong. Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                break

    user_request5 = input("Do you wish to try again? Y/N: ")
    if user_request5 in r:
        user_request6 = input("Pick your Pokeball - Pokeball or Greatball: ")
        if user_request6 in pokeball:
            print("-------\nYou now have 13x Pokeballs remaining")
            print("-------\nYou throw your Pokeball at Zubat..")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("You have successfully captured Zubat!")
            end = input("Would you like to battle or go to the shop? Type 'Battle' or 'Shop': ")
            if end in battle5:
                from battle import Battle
                print(Battle())
            if end in gotoshop:
                from shop import Go_Shop
                print(Go_Shop())
        if user_request6 in greatball:
            print("------\nYou now have 3x Greatballs remaining")
            print("You throw your Greatball at Zubat..")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            print("You have successfully captured Zubat!")
            end = input("Would you like to battle or go to the shop? Type 'Battle' or 'Shop': ")
            if end in battle5:
                from battle import Battle
                print(Battle())
            if end in gotoshop:
                from shop import Go_Shop
                print(Go_Shop())
            
        if user_request5 in g:
            choice2 = input("Want to catch Gastly instead or go to the Pond?\nType 'Gastly' for Gastly or 'Pond' for Pond: ")
            if choice2 in gastly:
                from Gastly import Gastly_Option
                print(Gastly_Option)
            else:
                return Zubat_Option()
            if choice2 in pond_return:
                from Pond import Pond_Option
                print(Pond_Option)
            else:
                return Zubat_Option()
print(Zubat_Option())
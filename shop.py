import time 
from items import items
x = 1
y = 2 
z = 3
coins = 100 
Y = ["Y", "y", "Yes", "yes"]
N = ["N", "n", "No", "no"]
Ability_Shield = ["Ability Shield" , "ability shield" , "1" ]
Berries = ["Berries" , "berries" , "2"]
Food = ["Food" , "food" "3"]
Heal_Potion = ["Heal Potion" , "heal potion" , "4"]
Lucky_Egg = ["Lucky Egg" , "lucky egg" , "5"]
Pokeball = ["Pokeball", "pokeball" , "6"]

def Go_Shop():
    print("-------\nThis is the Go Shop, life of paradise for the need of your pokemon(s) ")
    time.sleep(y)
    user_request1 = input("Would you like to purchase fellow Trainee? ")
    time.sleep(y)
    if user_request1 in Y:
        print(" The items in stock are listed ")
        print(" 1)  Ability Shield ")
        print(" 2)  Berries ")
        print(" 3)  Food")
        print(" 4)  Heal Potion ")
        print(" 5)  Lucky Egg ")
        print(" 6)  Pokeball (Normal)")
        time.sleep(y)
        purchase = input("Enter what you would like to purchase ")
        print(purchase) 
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue shopping? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()

    if purchase in Ability_Shield:
        print(" You have selected an Ability Shield")
        print("     Use: A one time use item, Helpful for defense in pokemon battles. It counters any attack with the opposing. ")
        print("     Amount: 25 coins ")
        user_request2 = input("     Would you like to purchase this item? ")
        if user_request2.upper() in Y:
            print("New balance is", coins - 25)
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()

    
    if purchase in Berries:
        print(" You have selected berries ")
        print("     Use: Berries are a helpful source of healing for your pokemon, improving the overall stats. ")
        print("     Amount: 25 coins ")
        user_request3 = input("     Would you like to purchase this item? ")
        if user_request3.upper() == Y:
            print(f"Current coins amount is" , coins - 25 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()

    
    if purchase in Food:
        print(" You have selected food")
        print("     Use: Food is good for maintaing  ")
        print("     Amount: 25 coins ")
        user_request4 = input("     Would you like to purchase this item? ")
        if user_request4.upper() == Y:
            print(f"Current coins amount is" , coins - 25 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()


    if purchase in Heal_Potion:
        print(" You have selected a Heal Potion")
        print("     Use: Heal potion is a good item for battling. When your pokemon is low on health, provide this delicious drink for them and their health increase ")
        print("     Amount: 45 coins ")
        user_request5 = input("     Would you like to purchase this item? ")
        if user_request5.upper() == Y:
            print(f"Current coins amount is" , coins - 45 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()


    if purchase in Lucky_Egg:
        print(" You have selected a Lucky Egg ")
        print("     Use: Good for beginner Trainees. This special tiems helps boost XP  ")
        print("     Amount: 30 coins ")
        user_request6 = input("     Would you like to purchase this item? ")
        if user_request6.upper() == Y:
            print(f"Current coins amount is" , coins - 30 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()


    if purchase in Pokeball:
        print(" You have selected a Pokeball ")
        print("     Use: Pokeballs are the basic need for catching Pokemons. Pokeballs(Normal) increase your chance of catching one. ")
        print("     Amount: 25 coins ")
        user_request7 = input("     Would you like to purchase this item? ")
        if user_request7.upper() == Y:
            print(f"Current coins amount is" , coins - 25 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue? Y/N: ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()


Go_Shop()
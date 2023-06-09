import time 

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
    time.sleep(1.5)
    user_request1 = input("Would you like to purchase fellow Trainee? ")
    time.sleep(1.5)
    if user_request1 in Y:
        print("-------\n")
        from items import Item
        time.sleep(1.5)
        purchase = input("Enter what you would like to purchase: ")
        print(purchase)
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue or battle? Y or 'Battle': ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()
            if (q== "Battle" or q== "battle" or q=="BATTLE" or q=="b"):
                x = False
                from battle import Battle
                print(Battle)

    if purchase in Ability_Shield:
        print("-------\nYou have selected an Ability Shield")
        print("     Use: A one time use item, Helpful for defense in pokemon battles. It counters any attack with the opposing.")
        print("     Amount: 25 coins ")
        user_request2 = input("     Would you like to purchase this item? ")
        if user_request2.upper() in Y:
            print("New balance is", coins - 25)
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue or battle? Y or 'Battle': ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()
            if (q== "Battle" or q== "battle" or q=="BATTLE" or q=="b"):
                x = False
                from battle import Battle
                print(Battle)

    
    if purchase in Berries:
        print("-------\nYou have selected berries ")
        print("     Use: Berries are a helpful source of healing for your pokemon, improving the overall stats.")
        print("     Amount: 5 coins ")
        user_request3 = input("     Would you like to purchase this item? ")
        if user_request3.upper() == Y:
            print(f"Current coins amount is", coins - 5 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue or battle? Y or 'Battle': ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()
            if (q== "Battle" or q== "battle" or q=="BATTLE" or q=="b"):
                x = False
                from battle import Battle
                print(Battle)

 
    if purchase in Food:
        print("-------\nYou have selected food")
        print("     Use: Food is good for maintaing and boosting the stats of your Pokemon.")
        print("     Amount: 25 coins ")
        user_request4 = input("     Would you like to purchase this item? ")
        if user_request4.upper() == Y:
            print(f"Current coins amount is", coins - 25 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue or battle? Y or 'Battle': ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()
            if (q== "Battle" or q== "battle" or q=="BATTLE" or q=="b"):
                x = False
                from battle import Battle
                print(Battle)


    if purchase in Heal_Potion:
        print("-------\nYou have selected a Heal Potion")
        print("     Use: Heal potion is a good item for battling. When your pokemon is low on health, provide this delicious drink for them and their health increase.")
        print("     Amount: 15 coins ")
        user_request5 = input("     Would you like to purchase this item? ")
        if user_request5.upper() == Y:
            print(f"Current coins amount is", coins - 15)
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue or battle? Y or 'Battle': ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()
            if (q== "Battle" or q== "battle" or q=="BATTLE" or q=="b"):
                x = False
                from battle import Battle
                print(Battle)

    if purchase in Lucky_Egg:
        print("-------\nYou have selected a Lucky Egg ")
        print("     Use: Good for beginner Trainees. This special tiems helps boost XP.")
        print("     Amount: 30 coins ")
        user_request6 = input("     Would you like to purchase this item? ")
        if user_request6.upper() == Y:
            print(f"Current coins amount is",coins - 30 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue or battle? Y or 'Battle': ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()
            if (q== "Battle" or q== "battle" or q=="BATTLE" or q=="b"):
                x = False
                from battle import Battle
                print(Battle)

    if purchase in Pokeball:
        print("-------\nYou have selected a Pokeball ")
        print("     Use: Pokeballs are the basic need for catching Pokemons. Pokeballs(Normal) increase your chance of catching one.")
        print("     Amount: 25 coins ")
        user_request7 = input("     Would you like to purchase this item? ")
        if user_request7.upper() == Y:
            print(f"Current coins amount is",coins - 25 )
    else:
        x = True    
        while x == True:
            q = input("Would you like to continue or battle? Y or 'Battle': ")
            if (q== "Y" or q== "Yes" or q=="y" or q=="yes"):
                x = False
                return Go_Shop()
            if (q== "Battle" or q== "battle" or q=="BATTLE" or q=="b"):
                x = False
                from battle import Battle
                print(Battle)

Go_Shop()
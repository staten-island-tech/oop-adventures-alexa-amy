import time 

x = 1
y = 2 
z = 3 
Y = ["Y", "y", "Yes", "yes"]
N = ["N", "n", "No", "no"]
Ability_Shield = ["Ability Shield" , "ability shield" , "1" ]
Berries = ["Berries" , "berries" , "2"]
Food = ["Food" , "food" "3"]
Heal_Potion = ["Heal Potion" , "heal potion" , "4"]
Lucky_Egg = ["Lucky Egg" , "lucky egg" , "5"]
Pokeball = ["Pokeball", "pokeball" , "6"]
continue2 = ["Continue", "continue"]
coins = 100
x = True

print("-------\nThis is the Go Shop, life of paradise for the need of your pokemon(s) ")
time.sleep(y)
user_request1 = input("Would you like to purchase fellow Trainee? ")
time.sleep(y)

def Go_Shop():
    while x == True:
        if user_request1 in Y:
            print(" The items in stock are listed ")
            print(" 1)  Ability Shield ")
            print(" 2)  Berries ")
            print(" 3)  Food")
            print(" 4)  Heal Potion ")
            print(" 5)  Lucky Egg ")
            print(" 6)  Pokeball (Normal)")
        time.sleep(1.5) 
        purchase = input("What you would like to purchase?: ")
        if purchase in Ability_Shield:
            print(" You have selected an Ability Shield")
            print("     Use: A one time use item, Helpful for defense in pokemon battles. It counters any attack with the opposing. ")
            print("     Amount: 25 coins ")
            user_request2 = input("     Would you like to purchase this item? ")
            if user_request2.upper() == "Y":
                coins = coins - 25
                print("New balance is", coins)

        if purchase in Berries:
            print(" You have selected berries ")
            print("     Use: Berries are a helpful source of healing for your pokemon, improving the overall stats. ")
            print("     Amount: 25 coins ")
            user_request3 = input("     Would you like to purchase this item? ")
            if user_request3.upper() == "Y":
                coins = coins - 25
                print("Current coins amount is" , coins)

        if purchase in Food:
            print(" You have selected food")
            print("     Use: Food is good for maintaing  ")
            print("     Amount: 25 coins ")
            user_request4 = input("     Would you like to purchase this item? ")
            if user_request4.upper() == "Y":
                coins = coins - 25
                print("Current coins amount is" , coins)

        if purchase in Heal_Potion:
            print(" You have selected a Heal Potion")
            print("     Use: Heal potion is a good item for battling. When your pokemon is low on health, provide this delicious drink for them and their health increase ")
            print("     Amount: 45 coins ")
            user_request5 = input("     Would you like to purchase this item? ")
            if user_request5.upper() == Y:
                coins = coins - 45
                print("Current coins amount is" , coins)


        if purchase in Lucky_Egg:
            print(" You have selected a Lucky Egg ")
            print("     Use: Good for beginner Trainees. This special tiems helps boost XP  ")
            print("     Amount: 30 coins ")
            user_request6 = input("     Would you like to purchase this item? ")
            if user_request6.upper() == Y:
                coins = coins - 30
                print("Current coins amount is" , coins)


        if purchase in Pokeball:
            print(" You have selected a Pokeball ")
            print("     Use: Pokeballs are the basic need for catching Pokemons. Pokeballs(Normal) increase your chance of catching one. ")
            print("     Amount: 25 coins ")
            user_request7 = input("     Would you like to purchase this item? ")
            if user_request7.upper() == Y:
                coins = coins - 25
                print("Current coins amount is" , coins)

    
    if user_request1 in N:
        print("Don't waste time here then ")
        print("Go catch them all! ")
print(Go_Shop())

""" pokeballs = print(" You have selected Pokeball ") """
""" else:
            shop_return = input("Would you like to continue purchasing or battle Mr. Whalen?: ")
            if shop_return in continue2:
                return Go_Shop """
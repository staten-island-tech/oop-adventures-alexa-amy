import time 
from items import items
x = 1
y = 2 
z = 3
purchase = ("p")
coins = 100 
Y = ["Y", "y", "Yes", "yes"]
N = ["N", "n", "No", "no"]

""" p1 = Person("John", 36)

print(p1.name)
print(p1.age) """

print("This is the Go Shop, life of paradise for the need of your pokemon(s) ")
time.sleep(y)
user_request1 = input("Would you like to pruchase fellow Trainee? ")
time.sleep(y)
if user_request1 in Y:
    print(" The items in stock are listed ")
    print("     Ability Shield ")
    print("     Berries ")
    print("     Food")
    print("     Heal Potion ")
    print("     Lucky Egg ")
    print("     Pokeball ")
    time.sleep(y)
    purchase = input("Enter what you would like to purchase ")
else:
    print("Don't waste time here then ")
    print("Go catach them all! ")




if purchase == ("berries"):
    print(" You have selected berries ")
    print("     Use: Berries are a helpful source of healing for your pokemon, improving the overall stats. ")
    print("     Amount: 25 coins ")
    user_request1 = print("     Would you like to purchase this item? ")
    if user_request1.upper == Y:
        print(f"Current coins amount is" , coins - 25 )
        
""" pokeballs = print(" You have selected Pokeball ") """


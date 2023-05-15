import time
import random
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Player(User):
    def __init__(self, name, coins):
        super().__init__(id,name)
        self.coins = coins
    def __str__(self):
        return f"{self.name}, {self.coins}"

class NPC(User):
    def __int__(self, name, trainer):
        super(). __int__(name, trainer )

print('Hello trainee, what a thrilling day to be out here with your battles ')
time.sleep(2)
user_input = input('Well then, want to battle it out to earn EXP? ')
if user_input.upper() == "Y":
    print("Okay, I will let you prepare first")
    time.sleep(2)
    print("Enter 3 pokemons to battle")
pokemon = []
add_more_pokemon = "Y"
while add_more_pokemon == "Y":
    user_request = input("Would you like to add another pokemon? ")
    if user_request.upper() == "Y": 
        pokemon_r = input("Enter name of a pokemon ")
    else:
        print("Something went wrong, are you sure you typed the request correctly? ")  
    still_continue = input("Would you like to continue? Y/N: ")
    add_more_pokemon = still_continue
    pokemon.append(pokemon_r)
print(f"your team consists of: {pokemon}")
print("Ready to battle Mr.Whalen? Y/N")
if print.upper() == "Y":
    print("Ready when you are ")
else: 
    print("Well, I'm ready so you are now ") #hold 

time.sleep(2)
Battles = 0 
while (Battles <= 0):
    print("1) attack Mr.Whalen's {random_pokemon} 2) Abide 3) healing 4)Switch to 



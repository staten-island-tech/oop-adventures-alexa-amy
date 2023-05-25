import time
import random
x = 1 
y = 2
z = 3

print('Hello trainee, what a thrilling day to be out here with your battles ')
time.sleep(y)
user_input = input('Well then, want to battle it out to earn EXP? ')
if user_input.upper() == "Y":
    print("Okay, I will let you prepare first")
    time.sleep(y)
    print("Enter 3 pokemons to battle")
pokemon = []
add_more_pokemon = "Y"
while add_more_pokemon == "Y":
    user_request = input("Would you like to add another pokemon? ")
    if user_request.upper() == "Y": 
        pokemon_r = input("Enter name of a pokemon: ")
    else:
        print("Something went wrong, are you sure you typed the request correctly? ")  
    still_continue = input("Would you like to continue? Y/N: ")
    add_more_pokemon = still_continue
    pokemon.append(pokemon_r)
print(f"your team consists of: {pokemon}")
time.sleep(y)
user_request = input("Ready to battle Mr.Whalen? Y/N ")
if user_request.upper() == "Y":
    print("Ready when you are ")
else: 
    print("Well, I'm ready so you are now ")

#hold 

time.sleep(y)
team = [pokemon]
switch = [pokemon]
pchoice= ["Primeape" ,"Snorlax"]
op1 = ["Good job! you Mr.Whalen's pokemon hp dropped by 5 " , "Missed AHHAHAHA "]
op3 = ["Your haling potion succeed and your pokemon gains 5 hp " ,  "Your healing potion failed, Mr.Whalen's turn now" ]
Battles = 0 
user_health = 100 
attack_request = "1", "2", "3", "4"
while (Battles <= 1):
    random_pokemon = (random.choice(pchoice))
    attack_request = input(f"Choose your move Trainee: 1) attack Mr.Whalen's {random_pokemon} 2) Abide 3) healing 4)Switch to {pokemon} ")
    if attack_request == "1":
        print(random.choice(op1))
        time.sleep(y)
    if attack_request == "2": 
        print("Move wasted ")
        time.sleep(z)
    if attack_request == "3": 
        print(random.choice(op3))
        time.sleep(y)
    if attack_request == "4": 
        print(f"Which pokemon do you want to use: {team}")
        time.sleep(z)
        attack_request = print(f"Detected, now switching to {switch}")
else:
    print("Are you sure you chose a correct option? Enter again ")
    still_continue = input("What attack method do you want? ")
    attack_request = still_continue
    
if (user_health) == 0:
    print("Mr.Whalen: HAAHWAH I WON! ")
    time.sleep(x)
    print("Better next time, trainee ")

if (Battles >= 1):
    print("Mr.Whalen: Oh man you beat my pokemons, see ya next time trainee! ")
    time.sleep(x)
    print("Good job trainee! Until next time, your next adventure awaits ")






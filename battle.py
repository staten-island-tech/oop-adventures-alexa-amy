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
user_health = 100 
MW_health = 100
pchoice= ["Primeape" ,"Snorlax"]
op1 = ["Good job! you Mr.Whalen's pokemon hp dropped by 5.", "Missed AHHAHAHA "]
op3 = ["Your healing potion succeed and your pokemon gains 5 hp " ,  "Your healing potion failed, Mr.Whalen's turn now" ]
Battles = 0 

attack_request = ["1", "2", "3"]
while (Battles <= 1):
    random_pokemon = (random.choice(pchoice))
    attack_request = input(f"Choose your move Trainee:\n1) Attack Mr.Whalen's {random_pokemon}\n2) Abide\n3) Return")
    if attack_request == "1":
        print(random.choice(op1))
        if random.choice(op1) == "Good job! you Mr.Whalen's pokemon hp dropped by 5.":
            MW_health = MW_health - 5
            print("Mr.Whalen's current health is",MW_health)
        if random.choice(op1) == "Missed AHHAHAHA ":
            print("maybe next time...")
    time.sleep(y)
    user_health = user_health - 5
    print("Mr. Whalen attacked -5 Hp, current health:" ,user_health)
    
    if attack_request in attack_request[2]: 
        print("Move wasted")
        time.sleep(z)    
    if attack_request in attack_request[3]: 
        print(random.choice(op3))
        time.sleep(y)
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

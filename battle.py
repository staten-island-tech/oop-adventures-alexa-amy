import time
import random

r = ["Y", "y", "Yes", "yes"]
g = ["N", "No", "n", "no"]
pokemon = []
team = [pokemon]
op1 = ["Good job! Mr.Whalen's pokemon hp dropped by 30", "Missed AHHAHAHA"]
op3 = ["Your healing potion succeeded\nYour pokemon gains 5 hp", "Your healing potion failed, Mr.Whalen's turn now"]
op4 = ["Battle", "battle", "BATTLE"]
op5 = ["Shop", "shop", "SHOP"]
attack_request = "1", "2", "3", "4"

def Battle():
    user_health = 100
    w_health = 100
    time.sleep(1.5)
    while w_health > 0:
        attack_request = input("-------\nChoose your move Trainee\n1) Attack Mr.Whalen's Snorlax\n2) Abide\n3) Healing\nEnter the corresponding number:  ")
        if attack_request == "1":
            print(random.choice(op1))
            if random.choice(op1) == "Good job! Mr.Whalen's pokemon hp dropped by 30!":
                w_health = w_health - 30
                time.sleep(1)
                print("Mr. Whalen's Snorlax hp is",w_health)
                time.sleep(1.5)
                print("Mr. Whalen uses tackle\nYour Pokemon lost 40 hp")
                user_health = user_health - 40
                time.sleep(1.5)
                print("Your Pokemon health",user_health)
            else:
                if random.choice(op1) == "Missed AHHAHAHA":
                    print("Mr. Whalen uses bite")
                    user_health = user_health - 25
                    time.sleep(1.5)
                    print("Your Pokemon health",user_health)
        
        if attack_request == "2": 
            time.sleep(1.5)
            print("Move wasted, Mr. Whalen uses a healing potion\nMr.Whalen's Snorlax gained 5 hp")
            w_health = w_health + 5
            time.sleep(1.5)
            print("Mr. Whalen's Snorlax hp is",w_health)
        
        if attack_request == "3": 
            print(random.choice(op3))
            if random.choice(op3) == "Your healing potion succeeded\nYour pokemon gains 5 hp":
                user_health = user_health + 10
                time.sleep(1.5)
                print("Your Pokemon health",user_health)
            else:
                user_health = user_health - 30
                time.sleep(1.5)
                print("Mr.Whalen uses Rollout\nYour Pokemon hp dropped by 30")
                time.sleep(1.5)
                print("Your Pokemon health is",user_health)
    
        if(user_health) == 0:
            print("Mr.Whalen wins!")
            time.sleep(1.5)
            battle_again = input("-------\nWould you like to battle Mr.Whalen again or go to the shop?\n'Battle' to try again or 'Shop' to go to the shop: ")
            if battle_again in op4:
                return Battle
            elif battle_again in op5:
                import shop
        if(w_health) == 0:
            print("You beat Mr. Whalen! Congrats")
            w_health = False
            break
    
    else:
        print("Are you sure you chose a correct option? Enter again: ")
        still_continue = input("What attack method do you want to use? ")
        attack_request = still_continue
print(Battle())
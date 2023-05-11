class User:
    def __init__(self, id, name, pokemon):
        self.id = id
        self.name = name
        self.pokemon = pokemon

class Player(User):
    def __init__(self, id, name, coins):
        super().__init__(id,name)
        self.coins = coins
    def __str__(self):
        return f"{self.name}, {self.coins}"

class NPC(User):
    def __int__(self, name, trainer):
        super(). __int__(name, trainer, pokemon)

pokemon = []
add_more_pokemon = "Y"
while add_more_pokemon == "Y":
    user_request = input("Would you like to add another pokemon? ")
    if user_request.upper() == "Y":
        pokemon = input("Enter name of a pokemon ")
    else:
        print("Something went wrong, are you sure you typed the request correctly? ")
        continue  
    still_continue = input("Would you like to continue? Y/N: ")
    add_more_pokemon = still_continue

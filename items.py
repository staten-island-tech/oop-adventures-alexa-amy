import time

class Item: 
    def __init__(self, name, amount, cost):
        self.name = name
        self.amount = amount  
        self.cost = cost

    def intro(self):
        print(f"{self.name} - Currently {self.amount} available! : {self.cost} coins")
    
    def show(self):
        print(f"Name : {self.name} - Boost: {self.boost} -- Currently {self.amount} available!")

    def show2(self):
        print(f"Name : {self.name} - Type of food: {self.type} -- Currently {self.amount} available!")
   
class Ability_Shield(Item):
    def use(self):
        print("     Use: A one time use item, Helpful for defense in pokemon battles. It counters any attack with the opposing.\n-------")

class Heal_Potion(Item):
    def use(self):
        print("     Use: Heal potion is a good item for battling. When your pokemon is low on health, provide this delicious drink for them and their health increase.\n-------")

class Lucky_Egg(Item):
    def use(self):
        print("     Use: Good for beginner Trainees. This special tiems helps boost XP.\n-------")

class Pokeball(Item):
    def use(self):
        print("     Use: Pokeballs are the basic need for catching Pokemons. Pokeballs(Normal) increase your chance of catching one.\n-------")

class Food(Item):
    def __init__(self, name, boost, amount, cost):
        super().__init__(name, amount, cost)
        self.boost = boost
    
    def use(self):
        print("     Use: Food is good for maintaing and boosting the stats of your Pokemon.\n-------")

    def show(self):
        print(f"{self.name} - Boost: {self.boost} -- Currently {self.amount} available! : {self.cost} coins")

class Berries(Item):
    def __init__(self, name, type, amount, cost):
        super().__init__(name, amount, cost)
        self.type = type
    
    def use(self):
        print("     Use: Berries are a helpful source of healing for your pokemon, improving the overall stats.\n-------")
    
    def show2(self):
        print(f"{self.name} - Type of food: {self.type} -- Currently {self.amount} available! : {self.cost} coins")

a = Ability_Shield(" 1)  Ability Shield", 10, 25)
a.intro()
a.use()
time.sleep(2)
b = Berries(" 2)  Berries", "Berries", 25, 5)
b.show2()
b.use()
time.sleep(2)
c = Food(" 3)  Food", "+10 in Defense!", 15, 25)
c.show()
c.use()
time.sleep(2)
d = Heal_Potion(" 4)  Heal Potion", 5, 15)
d.intro()
d.use()
time.sleep(2)
e = Lucky_Egg(" 5)  Lucky Egg", 2, 30)
e.intro()
e.use()
time.sleep(2)
f = Pokeball(" 6)  Pokeball", 15, 25)
f.intro()
f.use()

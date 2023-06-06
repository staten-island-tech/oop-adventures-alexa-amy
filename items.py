class items: 
     def __init__(self, name, amount):
        self.name = name
        self.amount = amount 
   
class Ability_Shield(items):
    def __int__(self, name, amount):
        super().__int__(name, amount)
    def __str__(items):
        return f"{items.name}, {items.amount}"

class Heal_Potion(items):
    def __int__(self, name, amount):
        super().__int__(name,amount)
    def __str__(items):
        return f"{items.name}, {items.amount}"

class Lucky_Egg(items):
    def __int__(self, name, amount):
        super().__int__(name,amount)
    def __str__(items):
        return f"{items.name}, {items.amount}"

class Pokeball(items):
    def __int__(self, name, amount):
        super().__int__(name,amount)
    def __str__(items):
        return f"{items.name}, {items.amount}"

class food(items):
    def __int__(self, name, amount):
        self.name = name 
        self.amount = amount 

class Berries(items):
    def __int__(self, name, amount):
        super().__int__(name, amount)
    def __str__(items):
        return f"{items.name}, {items.amount}"


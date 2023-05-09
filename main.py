class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Player(User):
    def __init__(self, id, name, coins):
        super().__init__(id,name)
        self.coins = coins
    def __str__(self):
        return f"{self.name}, {self.coins}"


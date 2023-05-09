class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Player(User):
    def __init__(self, id, name, coins):
        super().__init__(id,name)
        self.coins = coins
    def __str__(self):
<<<<<<< HEAD
        return f"{self.name}, {self.coins}"
=======
        return f"{self.name}, {self.coins}, {self.id}"
    

>>>>>>> d8958422bcc386a777663c48be25de452ac2f6cc


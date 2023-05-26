class User:
    def __init__(self, name, coins):
        self.name = name
        self.coins = coins

    def trainer(self):
        print("-------\nHello {}!".format(self.name))
        print("You currently have {} coins!".format(self.coins))
person = User(input("What is your name?: "), 100)
person.trainer()
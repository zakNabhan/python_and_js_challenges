class Account:
    """simple account class with balance"""
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("account created for"+ self.name)

    def deposit(self, amount):
        pass
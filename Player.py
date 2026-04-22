class Player:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet()

    def add_funds(self, amount):
        self.wallet.balance += amount

    def withdraw_funds(self, amount):
        if self.wallet.balance >= amount:
            self.wallet.balance -= amount
            return amount
        return 0

    def __str__(self):
        return f"Player(name={self.name}, balance={self.wallet.balance})"
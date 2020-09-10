class bankaccount():
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return print("total amount: ",self.balance)
    def withdraw(self, amount):
        if amount > self.balance:
            return print("total balance is low")
        else:
            self.balance-= amount
            return print("total balance: ",self.balance)

bank = bankaccount('John',25000)
bank.deposit(5000)
bank.withdraw(25000)
bank.deposit(500)
bank.withdraw(6000)

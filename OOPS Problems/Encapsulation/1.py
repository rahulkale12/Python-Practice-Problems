#1.Create a BankAccount class with a private attribute _balance. Provide methods deposit(), withdraw(), and get_balance() to access it safely.

class BankAccount:
    def __init__(self,balance):
        self._balance = balance   #private attribute
        print("Balance in account:",self._balance)

    def deposit(self,amount):
        if amount>>0:
            self._balance +=amount
            print(f"{amount}:Deposited")
        else:
            print("Invalid deposit amount")
    
    def withdraw(self,amount):
        if 0 < amount <=self._balance:
            self._balance -= amount
            print(f"{amount}:Withdrawn")
        else:
            print("Insufficeient fund")

    
    def get_balance(self):
        return self._balance

account = BankAccount(10000)
account.deposit(2000)
account.withdraw(1000)
print("Current Balance:",account.get_balance())
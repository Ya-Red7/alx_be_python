class BankAccount:
    def __init__(self,account_balance=0.00):
        self.account_balance = account_balance
        
    def deposit(self,amount):
        self.account_balance+= float(amount)
    def withdraw(self,amount):
        if amount>self.account_balance:
            return 0
        self.account_balance-=float(amount)
        return 1
    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")


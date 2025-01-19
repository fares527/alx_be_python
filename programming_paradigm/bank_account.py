class BankAccount:
    def __init__(self, account_balance=0.0):
        self.account_balance=account_balance
       
    def deposit(self , amount):
        if amount <=0 :
            raise ValueError("account balance must be positive number")
        self.account_balance += amount

    def withdraw(self, amount ):
         if amount <=0 :
            raise ValueError("account balance must be positive number")
         if amount > self.account_balance :
             return False
         self.account_balance -= amount

    def display_balance(self):
        print(f"The current balance = {self.account_balance: .2f} $ ") 
         
        
        
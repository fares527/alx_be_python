class BankAccount:
    def __init__(self, account_balance=0.0):
        self.current_balance=account_balance
       
    def deposit(self , amount):
        if amount <=0 :
            raise ValueError("current balance must be positive number")
        self.current_balance += amount

    def withdraw(self, amount ):
         if amount <=0 :
            raise ValueError("curent balance must be positive number")
         if amount > self.current_balance :
             return False
         self.current_balance -= amount

    def display_balance():
        print(f"current balance:") 
         
        
        
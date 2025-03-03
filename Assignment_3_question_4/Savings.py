#Savings (Child Class of Account)
#Additional Attributes:
#over_draft: Set to 1200 (overdraft limit).
#Additional Methods:
#profit(): Increments current_balance by 15% (profit is credited periodically).
from Account import Account
#Creating a child class Savings inheriting from class Account
class Savings(Account):

    def __init__(self, account_type, min_balance, current_balance,overdraft_limit):
        #Executing the constructor for the parent class
        super().__init__(account_type, min_balance, current_balance,overdraft_limit)
    #Method to create the profit
    def profit(self):
        self.current_balance += (self.current_balance * 0.15)
        print(f'The current balance after profit is: {self.current_balance}')
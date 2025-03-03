#Checking (Child Class of Account)
#Additional Attributes:
#over_draft: Set to 1000 (overdraft limit).
#Inherits the withdraw and deposit methods.
from Account import Account
#Creating a child class Checking inheriting from class Account
class Checking(Account):

    def __init__(self, account_type, min_balance, current_balance,overdraft_limit):
        #Creating a child class Checking inheriting from class Account
        super().__init__(account_type, min_balance, current_balance,overdraft_limit)

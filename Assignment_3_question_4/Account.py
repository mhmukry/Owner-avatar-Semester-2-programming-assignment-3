#Account (Parent Class)
#Attributes:
#Acct_type: Represents the type of account (e.g., "Checking" or "Savings").
#min_balance: A minimum balance requirement (default: 500).
#current_balance: Stores the current account balance.
#Methods:
#withdraw(amount): Decrements current_balance by amount. If the balance goes negative, it should check if the overdraft limit is exceeded.
#deposit(amount): Increments current_balance by amount.


class Account:
    #defining Account attributes
    account_type = "" 
    min_balance = 0
    current_balance = 0
    overdraft_limit= 0
    deposit_counter = 0



    def __init__(self, account_type, min_balance, current_balance,overdraft_limit):
        self.account_type = account_type
        self.min_balance = min_balance
        self.current_balance = current_balance
        self.overdraft_limit= overdraft_limit
    #Method to withdraw amount and also check if it is within overdraft limit
    def withdraw(self, withdraw_amount):
        #If withdrawal amount is less than current balance then decrease current total balance 
        # by subtracting withdrawal amount 
        if (self.current_balance - withdraw_amount)>= 0:
            self.current_balance -= withdraw_amount
            print(f'The current balance after withdrawal is: {self.current_balance}')
        else:
            #If the withdrawal amount results in current total amount greater than overdraft 
            # then reject with a warning message 
            if (self.current_balance - withdraw_amount) * -1 > self.overdraft_limit: 
                print(f'Overdraft limit exceeded: Cannot withdraw requested amount of ${withdraw_amount}')
            #Else if the withdrawal amount results in current total amount less than overdraft 
            # but less than 0 then withdraw the amount and update current total with a warning message 
            # and also increase overdraft limit by $200
            else:
                self.overdraft_limit += 200
                self.current_balance -= withdraw_amount
                print(f'Warning: You are using overdraft limit which is now increased to ${self.overdraft_limit}')                 
                print(f'Warning: Your current balance is: ${self.current_balance} ')            
    #Method to deposit the amount and increase the deposit counter by 1
    def deposit(self, deposit_amount):
            self.deposit_counter += 1
            self.current_balance += deposit_amount
            print(f'The current balance after deposit is: {self.current_balance}')

        
    
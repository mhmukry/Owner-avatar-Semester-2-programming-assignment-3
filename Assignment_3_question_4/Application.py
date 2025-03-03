from Account import Account
from Checking import Checking
from Savings import Savings
from Person import Person


class Application:
    #Initializing the empty customer/person list
    customer_list = []
    #Method to display main menu for customer
    def display_main_menu(self):
        user_choice = 0
        while user_choice != 3:
            print("********** Main Menu for Customer **********")           
            print("Press 1. To create new customer: ")
            print("Press 2. To select a customer from a list ")
            print("Press 3. To Exit the program ")
            user_choice = int(input("Enter your choice(1 or 2 or 3 ): "))
            #User chooses to create a new customer/person
            if user_choice == 1:
                person = self.create_new_customer()
                #If user successfully created a new customer/person then offer them options 
                # to perform to deposit/withdraw transactions 
                if person is not None:                
                    self.display_sub_menu_account_activities(person)
            #User chooses to select an existing customer/person 
            elif user_choice == 2:
                person = self.list_customer()
                #If user selects a valid existing customer/person then offer them options 
                # to perform to deposit/withdraw transactions
                if person is not None:
                    self.display_sub_menu_account_activities(person)
    #Method to display sub menu for customer/person to perform deposit/withdraw transactions
    def display_sub_menu_account_activities(self, person):
        user_choice = 0
        while user_choice != 3:
            print("********** Sub Menu for Transactions **********")           
            print("Press 1. To Deposit amount: ")
            print("Press 2. To Withdraw amount: ")
            print("Press 3. To Exit back to Main Menu")
            user_choice = int(input("Enter your choice(1 or 2 or 3 ): "))
            #If user choose to deposit amount
            if user_choice == 1:
                deposit_amount = int(input("Enter amount to deposit: "))
                person.account.deposit(deposit_amount)
                #Condition to check if customer is eligible for profit 
                if (person.account.account_type == "Savings") and (person.account.deposit_counter == 10):
                     person.account.profit()
                     person.account.deposit_counter = 0
             #If user choose to withdraw amount                    
            elif user_choice == 2:
                withdraw_amount = int(input("Enter amount to withdraw: "))
                person.account.withdraw(withdraw_amount)

    #Method to create new customer/person and add them to customer/person list
    def create_new_customer(self):
        account = None
        customer_name = input("Enter customer name: ")
        account_type = input("Type of account to open(Savings/Checking): ")
        #If user selects Savings account type then create Savings account with the 
        # default minimum balance and overdraft limit for Savings account
        if account_type == "Savings":
            account = Savings("Savings", 500, 0, 1200)
        #If user selects Checking account type then create Checking account with the 
        # default minimum balance and overdraft limit for Checking account            
        elif account_type == "Checking":
            account = Checking("Checking", 500, 0, 1000)
        #If user selected the correct account types and Account is successfully created 
        # then create a new customer with the provided name and account type 
        if account is not None:
            person = Person(customer_name, account)
            self.customer_list.append(person)
            return person
    #Method to list existing customers/persons and select customer /person from the list
    def list_customer(self):
        for person in self.customer_list:
            print(f'Person| account type | min balance | current balance | overdraft limit')
            print(f'{person.name} |  {person.account.account_type} | {person.account.min_balance} | {person.account.current_balance} | {person.account.overdraft_limit} |')
        #If any customer exists then request the option to select customer
        if len(self.customer_list) > 0:
            selected_customer_name = input("Enter customer to select: ") 
            for person in self.customer_list:
                if person.name == selected_customer_name:
                    return  person
        # Else notify that no customer exists
        else:
            print(f'No customers exist!')    

    #Method to run the main menu options
    def run(self):
        self.display_main_menu()     

if __name__ == "__main__":
    app = Application()
    app.run()

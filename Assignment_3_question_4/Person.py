#Person Class
#Attributes:
#name: Stores the name of the person.
#account: An instance of either Checking or Savings.

from Account import Account 

class Person:
    #defining Person attributes
    name = ""
    account = Account
    #Constructor to create Person object
    def __init__(self, name, account):
        self.name = name
        self.account = account
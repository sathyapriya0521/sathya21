'''implement a class called bank account that represents a bank account.The class should have private
attributes for account number,account holdername, and account balance.Include methods to
deposit money,withdraw money,and display the account balance.Ensure that the account balance
cannot be accessed directly from outside the class.Write a program to create an instance of the 
bank account class and the test the deposit and withdrawal functionality.'''


class bankaccounts:

def__init__(self,account_number,account_holder_name,initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance
        
def deposit(self,amount):
if amount>0:
self.__account_balance+=amount
#self.__account_balance=self.__account_balance+amount
printf("Deposited ${}. New balance:${}".format(amount,
self.__account_balance))
else:
printf("invalid depoist amount. please deposit a positive amount.")

def withdraw(self,amount):
if amount>0and amount<=self.__account_balance:
self.__account_balance-=amount
#self.__account_balance=self.__account_balance-amount
printf("withdraw ${}".format(amount,
                                self.__account_balance))
else:
printf("invalid withdrawal amount or insufficient balance.")

def display_balance(self):
printf("account balance for {} (account #{}".format(
    self.__account_holder_name,self.__account_number,
    self.__account_balance))

    
# create an instance of the bank account class
account=bank account(account_number="123456789",
account_holder_name="hari prabu",
initial_balance=5000.0)

# test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdrawal(200.0)
account.display_balance()
# unsing encapsulation method // restricting certain part of object's
# create bank account and make balance private

# freature
#     1. create bank account class
#     2. keep balance private
#     3. provide method to deposite, withdraw and check balance


class BankAccount():
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__initial_balance = initial_balance    # to make this private use __ double underscore at starting of variale name
        self.__transactions = []
    def deposite(self, amount):
        if amount > 0:
            self.__initial_balance += amount
            self.__transactions.append(f"Deposited: {amount}")
            print(f"Deposited: {amount}")
        else:
            print("Deposite must be positive. Try again...")
    
    def withdraw(self, amount):
        if amount > self.__initial_balance:
            print("Insufficient Funds")
            self.__transactions.append(f"Failed withdrawal: {amount} Insufficient fund")
        elif amount > 0:
            self.__initial_balance -= amount
            self.__transactions.append(f"Withdrawal amount: {amount}")
            print(f"Withdew: {amount} remaining is {self.__initial_balance}")
        else:
            print("Withdral amount must be positive. Try again ...")
            
    
    def getBlance(self):
        return f"{self.account_holder}'s Current balance: {self.__initial_balance}"
    
    def getTransactionHistory(self):
        print(f"Transaction history of {self.account_holder}")
        for transaction in self.__transactions:
            print(transaction)
    
    
    
#  object intialtion
account1 = BankAccount("Manohar", 100000)
account2 = BankAccount("Sanjiv", 1000)


# Methods call
print(account1.getBlance())

account1.deposite(100)
print(account1.getBlance())

account1.withdraw(5000)
print(account1.getBlance())


print(account2.getBlance())

account2.deposite(-50000)
print(account2.getBlance())

account2.withdraw(90000)
print(account2.getBlance())
account2.withdraw(50)
print(account2.getBlance())

account1.getTransactionHistory()
account2.getTransactionHistory()



# add fuctionality to see transaction history
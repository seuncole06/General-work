class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount):
        if amount > 0:
             self.__balance += amount
             print("Deposit successfully")
        else:
            print("Invalid Transaction")

account1 = BankAccount(500000)

account1.deposit(100000)

print(account1.get_balance())

#Public	    name	Freely accessible
#Protected	_name	Intended for internal use
#Private	__name	Name mangling restricts direct access
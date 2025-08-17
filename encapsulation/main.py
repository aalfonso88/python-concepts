class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private attribute (hidden)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        return "Not enough funds"

    def get_balance(self):
        return self.__balance
    

class Example:
    def __init__(self):
        self._internal = "use with care"     # protected by convention
        self.__hidden = "name mangled"       # harder to access


################
obj = Example()

print(obj._internal)         # works, but "not recommended"
# print(obj.__hidden)        # AttributeError


account = BankAccount(100)
account.deposit(50)
print(account.get_balance())  # 150

# Direct access is prevented
print(account.__balance)  # AttributeError
class Account:
    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        try:
            if amount <= 0:
                return False
            else:
                self.__account_balance += amount
                return True
        except ValueError:
            print('Invalid input.')

    def withdraw(self, amount):
        try:
            if amount <= 0:
                return False
            elif amount > self.__account_balance:
                return False
            else:
                self.__account_balance -= amount
                return True
        except ValueError:
            print('Invalid input.')

        def get_balance(self):
            return self.__account_balance

        def get_name(self):
            return self.__account_name
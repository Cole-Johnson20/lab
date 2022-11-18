class Account:
    def __init__(self, name: str) -> None:
        """
        Constructs all necessary values for the Account class
        :param name: The name that is associated with the account
        """
        self.__account_name = str(name)
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Allows the user to deposit money to the account i.e adding money to the account
        :param amount: Amount of money that the user wants deposited in their account
        :return:True if transaction is successful and False if transaction does not happen due to invalidity
        """
        try:
            if amount <= 0:
                return False
            else:
                self.__account_balance += amount
                return True
        except ValueError:
            print('Enter numeric values.')
        except:
            print('Invalid input')

    def withdraw(self, amount: float) -> bool:
        """
        Allows the user to withdraw money from the account i.e subtracting money from the account
        :param amount: Amount of money that
        :return:True if transaction is successful and False if transaction does not happen due to invalidity
        """
        try:
            if amount <= 0:
                return False
            elif amount > self.__account_balance:
                return False
            else:
                self.__account_balance -= amount
                return True
        except ValueError:
            print('Enter numeric values.')
        except:
            print('Invalid input')

    def get_balance(self) -> float:
        """
        Gets the total balance of the account
        :return:Total balance of the account
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Get the name associated with the account
        :return: Name of the account
        """
        return self.__account_name

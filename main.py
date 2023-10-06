class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
        self.__last_deposit_amount = 0
        self.__last_withdraw_amount = 0

    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
        self.__last_deposit_amount = deposit_amount

    def get_deposit(self):
        return self.__last_deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.__balance:
            print(f"Transaction cancelled! Current balance ({self.__balance})"
                  f"is less than the amount you're trying to withdraw.")
            self.__last_withdraw_amount = 0
        else:
            self.__balance -= withdraw_amount
            self.__last_withdraw_amount = withdraw_amount

    def get_withdraw(self):
        return self.__last_withdraw_amount


    def get_balance(self):
        return self.__balance


    def get_account_number(self):
        return self.__account_number


b1 = BankAccount(12345, 100)
print(b1.get_balance())
print(b1.get_account_number())


b1.deposit(100)
print(b1.get_balance())
print(b1.get_deposit())

b1.deposit(500)
print(b1.get_balance())
print(b1.get_deposit())

b1.withdraw(900)
print(b1.get_balance())

b1.withdraw(700)
print(b1.get_balance())
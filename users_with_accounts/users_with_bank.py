class  BankAccount:
    all_accounts = []

    def __init__(self, int_rate = 0.01, balance = 0):
        self.interest_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        
        return self
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print('You do not have enough funds to withdraw that amount. Charging a $5 fee')
            self.balance -= 5
        
        return self
    
    def display_account_info(self):
        print(f"Your current balance is: {self.balance}")

        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (self.balance * self.interest_rate)
        
        return self

    @classmethod
    def all_balances(cls):
        sum = 0

        for account in cls.all_accounts:
            sum += account.balance
        return sum

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self

user1 = User("Vincent", "Guerena")

user1.make_deposit(500).display_user_balance().make_withdrawal(250).display_user_balance()


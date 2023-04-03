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
    
account1 = BankAccount()
account1.deposit(25).deposit(75).deposit(100).withdraw(50).yield_interest().display_account_info()

account2 = BankAccount()
account2.deposit(150).deposit(300).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()

print(BankAccount.all_balances())


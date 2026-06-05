class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_id, initial_balance=0):
        if account_id in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[account_id] = initial_balance

    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.accounts[account_id] += amount

    def withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.accounts[account_id] < amount:
            raise ValueError("Insufficient funds.")
        self.accounts[account_id] -= amount

    def get_balance(self, account_id):
        if account_id not in self.accounts:
            raise ValueError("Account does not exist.")
        return self.accounts[account_id]
    
    
Brac_bank = Bank()
Brac_bank.create_account("12345", 1000)
Brac_bank.deposit("12345", 500) 
Brac_bank.withdraw("12345", 200)
balance = Brac_bank.get_balance("12345")
print(f"Current balance for account 12345: {balance}")


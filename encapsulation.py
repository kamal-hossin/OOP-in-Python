class BankAccount:

    # Constructor
    def __init__(self, name, account_number, balance):

        # Public Access Modifier
        self.name = name

        # Protected Access Modifier
        self._account_number = account_number

        # Private Access Modifier
        self.__balance = balance

    # Deposit Method
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount}  Deposit Successfully!")

    # Withdraw Method
    def withdraw(self, amount):

        if amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount
            print(f"{amount} টাকা Withdraw Successfully!")

    # Getter Method
    def get_balance(self):
        return self.__balance

    # Display Info
    def show_info(self):

        print("\n=== Bank Account Information ===")
        print(f"Name           : {self.name}")
        print(f"Account Number : {self._account_number}")
        print(f"Balance        : {self.__balance}")


# Object Create
user1 = BankAccount(
    "Kamal",
    "123456789",
    5000
)

print(user1.name)

print(user1._account_number)

user1.deposit(2000)

user1.withdraw(1000)

print(f"Current Balance: {user1.get_balance()}")

# Show Full Info
user1.show_info()
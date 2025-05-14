class Bank:
    bank_name = "National Bank"  # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Changing the class variable using cls

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

# Create instances
account1 = Bank("Ali")
account2 = Bank("Sara")

# Display initial bank name
account1.display()
account2.display()

print("\nChanging bank name...\n")
Bank.change_bank_name("International Bank")

# Display updated bank name for all instances
account1.display()
account2.display()

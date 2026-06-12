class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount: float) -> None:
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self) -> float:
        return self.balance

    def display(self) -> None:
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")
account = BankAccount("Aslam", 1000)

account.deposit(500)
account.withdraw(300)

account.display()

print("Current Balance:", account.get_balance())
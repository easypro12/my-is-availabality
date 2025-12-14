# -------- BankAccount CLASS (handles money only) --------
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₦{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew ₦{amount}")

    def show_balance(self):
        print(f"Current balance: ₦{self.balance}")


# -------- User CLASS (handles identity + login) --------
class User:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.account = BankAccount()   # each user gets one bank account

    def check_pin(self, entered_pin):
        return self.pin == entered_pin


# -------- BankSystem CLASS (controls input & flow) --------
class BankSystem:
    def __init__(self):
        self.users = []
        self.current_user = None

    # -------- Register --------
    def register(self):
        # username validation
        while True:
            username = input("Enter username: ").strip()
            if username:
                break
            print("Username cannot be empty")

        # pin validation
        while True:
            try:
                pin = int(input("Enter 4-digit PIN: "))
                if 1000 <= pin <= 9999:
                    break
                print("PIN must be 4 digits")
            except ValueError:
                print("PIN must be numbers only")

        user = User(username, pin)
        self.users.append(user)
        print("Registration successful\n")

    # -------- Login --------
    def login(self):
        username = input("Enter username: ").strip()

        try:
            pin = int(input("Enter PIN: "))
        except ValueError:
            print("Invalid PIN\n")
            return

        for user in self.users:
            if user.username == username and user.check_pin(pin):
                self.current_user = user
                print("Login successful\n")
                self.user_menu()
                return

        print("Wrong username or PIN\n")

    # -------- User Menu --------
    def user_menu(self):
        while self.current_user:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Logout")

            choice = input("Choose option: ")

            if choice == "1":
                self.handle_deposit()

            elif choice == "2":
                self.handle_withdraw()

            elif choice == "3":
                self.current_user.account.show_balance()

            elif choice == "4":
                self.current_user = None
                print("Logged out\n")

            else:
                print("Invalid option\n")

    # -------- Deposit handler --------
    def handle_deposit(self):
        try:
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive")
            else:
                self.current_user.account.deposit(amount)
        except ValueError:
            print("Enter numbers only")

    # -------- Withdraw handler --------
    def handle_withdraw(self):
        try:
            amount = int(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be positive")
            else:
                self.current_user.account.withdraw(amount)
        except ValueError:
            print("Enter numbers only")

    # -------- Main Menu --------
    def main_menu(self):
        while True:
            print("=== BANK SYSTEM ===")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.register()

            elif choice == "2":
                self.login()

            elif choice == "3":
                print("Goodbye")
                break

            else:
                print("Invalid option\n")


# -------- RUN PROGRAM --------
bank = BankSystem()
bank.main_menu()






















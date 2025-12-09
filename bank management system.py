class Banks:
    def __init__(self,name,account_no):
        self.name=name
        self.account_no=account_no

    def __str__(self):
        return f"name: {self.name} | account_no: {self.account_no}"


class Accounts:
    def __init__(self):
        self.banks=[]


    def add_account(self):
        name=input("enter account name:").lower()
        account_no=int(input("enter account number:"))
        new_banks=Banks(name,account_no)
        self.banks.append(new_banks)
        print("account added successfully")

    def remove_accounts(self):
        name=input("enter account name:").lower()
        for x in self.banks:
            if x.name==name:
                self.banks.remove(name)
                print("account removed successfully.\n")
                return
        print("account not found in bank.\n")


    def list_accounts(self):
        if  not  self.banks:
            print("account not found in bank.\n")

        else:
            print("\n --bank management system--")
            for x in self.banks:
                print(x)
            print()

def main_bank():
    my_accounts=Accounts()
    print("\n Bank Management System \n")
    print("1. add accounts")
    print("2.remove accounts")
    print("3.list accounts")
    print("4.exit")
    while True:
        option=input("enter option:")
        if option=="1":
            my_accounts.add_account()

        elif option=="2":
            my_accounts.remove_accounts()

        elif option=="3":
            my_accounts.list_accounts()

        elif option=="4":
            print("goodbye")
            break
        else:
            print("not a valid option")
main_bank()
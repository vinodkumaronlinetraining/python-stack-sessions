from wallet_package.data import *
from wallet_package.transactions import *
from wallet_package.profile import *
from wallet_package.auth import *
from wallet_package.storage import *
from datetime import datetime


def process_transaction(wallet):
    amount = float(input("Enter the amount:"))
    t_type = input("Enter the type (credit/debit): ")
    wallet.add_transaction(amount, t_type)
def main():

    # first_name = input("enter the first name: ")
    # last_name = input("Enter the last name: ")
    # address = input("Enter the Address: ")
    # password = input("Enter the password: ")

    # user1 = User(first_name, last_name, address, password)

    # auth = Auth()
    # wallet = Wallet(user1,auth)
    print("Welcome to wallet app!")
    first_name = input("Enter the first_name: ")
    last_name = input("Enter the last_name: ")

    record, transactions = Storage.load_user(first_name,last_name)

    if record:
        print(f"Welcome back,{first_name}")
        account_type = record["account_type"]
        if account_type == "Premium":

            user1 = PremiumUser(record["first_name"], record["last_name"], record["address"], record["password"])
        else:
            user1 = User(record["first_name"], record["last_name"], record["address"], record["password"])
        user1.wallet_balance = record["wallet_balance"]
        user1.is_active = record["is_active"]
        user1.cashback_balance = record.get("cashback_balance", 0.0)
    else:
        address = input("Enter the address: ")
        password = input("Enter the password: ")
        account_type = input("Enter the account type (Premium/Standard): ")
        if account_type == "Premium":
            user1 = PremiumUser(first_name,last_name,address,password)
        else:
            user1 = User(first_name,last_name,address,password)
        

    auth = Auth()
    wallet = PremiumWallet(user1,auth) if account_type == "Premium" else Wallet(user1, auth)
    wallet.user_transactions = transactions
    

    while True:
        print("1. Addtransaction ")
        print("2. view transaction History")
        print("3. Change password")
        print("4. Upadte profile")
        print("5. display user info")
        print("6. Account Summary")
        print("7. save and exit")

        choice = input("Enter the choice: ")

        if choice == '1':
            process_transaction(wallet)

        elif choice == '2':
            wallet.account_history()
            wallet.sort_transactions()
        elif choice == '3':
            new_password = input("Enter the new password: ")
            user1.set_password(new_password)
        elif choice == '4':
            key = input("Enter the attribute to be updated (first_name, last_name, address): ")
            value = input(f"Enter the value for {key}: ")
            user1.update_profile(key,value)
        elif choice == '5':
            user1.display_info()
        elif choice == '6':
            user1.get_account_summary()
        elif choice == '7':
            Storage.save_user(user1, wallet.user_transactions)
            print("Exiting menu ...")
            break
        else:
            print("Invalid input. Try again")

if __name__ == "__main__":
    main()

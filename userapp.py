from wallet_package.data import *
from wallet_package.transactions import *
from wallet_package.profile import *
from wallet_package.auth import *
from datetime import datetime

def main():

    first_name = input("enter the first name: ")
    last_name = input("Enter the last name: ")
    address = input("Enter the Address: ")
    password = input("Enter the password: ")

    user1 = User(first_name, last_name, address, password)

    auth = Auth()
    wallet = Wallet(user1,auth)

    while True:
        print("1. Addtransaction ")
        print("2. view transaction History")
        print("3. Change password")
        print("4. Upadte profile")
        print("5. display user info")
        print("6. exit")

        choice = input("Enter the choice: ")

        if choice == '1':
            amount = float(input("Enter the transaction amount: "))
            type = input("Enter type of transaction (credit/debit): ")
            wallet.add_transaction(amount, type)

        elif choice == '2':
            wallet.account_history()
        elif choice == '3':
            new_password = input("Enter the new password: ")
            user1.change_password(new_password)
        elif choice == '4':
            key = input("Enter the attribute to be updated (first_name, last_name, address): ")
            value = input(f"Enter the value for {key}: ")
            user1.update_profile(key,value)
        elif choice == '5':
            user1.display_info()
        elif choice == '6':
            print("Exiting menu ...")
            break
        else:
            print("Invalid input. Try again")

if __name__ == "__main__":
    main()

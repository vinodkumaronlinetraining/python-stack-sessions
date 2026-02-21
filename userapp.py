from wallet_package.data import *
from wallet_package.transactions import *
from wallet_package.profile import *
from datetime import datetime

def transaction_loop():
    while True:

        action = input(""" Choose an option: 
                            1. Add a Transaction
                            2. Transaction summary
                            3. Add a new pin
                            4. Update profile
                            5. change password
                            6. exit
                        Enter your choice here: """)
        if action == "1":
            print("------verifying user----------")
            # check_user_transaction()
            print("----------verifying transaction----------")
            # validate_transaction()
            print("-----Add a transaction-----")
            new_trans = float(input("Enter the transaction amount: "))
            
            add_transaction(new_trans)

        elif action == "2":
            print("---------Transaction summary---------")
            account_history()
            

        elif action == "3":
            print("---------add a new pin------------")
            new_pin = input(" Enter the new pin: ")
            add_pin(new_pin)

        elif action == "4":
            print(" --------------------update profile------------")
            new_key = input("Enter the new key: ")
            new_value = input("Enter the new value: ")
            update_profile(new_key= new_value)

        elif action == "5":
            print("----------change password----------")
            change_password()

        elif action == "6":
            print(" exiting...")
            break

        else:
            print("invalid input")
# transaction_loop()



def main():

    global user_transactions, user_cred, user_devices, user_profile,wallet_balance, is_active

    print("===========USer Wallet Application=================\n")

    # display initial data:
    display_user_info()
    print("-----------------------------------------")

    print(sum_transactions(user_transactions_array))

    debit_transactions = [ (amt , timestamp) for amt,timestamp in user_transactions if amt<0 ]
    print(debit_transactions)
    

    print("-----the Transaction loop-----------")
    transaction_loop()
    print("-----------------")

    # since all these functions are already called in the transaction_loop, commenting them here
    #-------------------------
    # # change password:
    # change_password()
    # print("----------------------------------------\n")

    # # add transaction:
    # new_transaction = float(input("Enter the transaction amount:"))
    # add_transaction(new_transaction)
    # print("----------------------------------\n")


    # # account statement:
    # print("-----------Account Statement-----------\n")
    # account_history()
    # print("----------------------------------\n")

    # # update details
    # new_key = input(" enter the new key:")
    # new_val = input("enter new value:")
    # update_profile(new_key,new_val)
    # print("--------------------------------\n")

    # penalty
    print("=========penalty added========")
    debit_penalty(50)
    print("--------------------------------\n")

    # interst
    print("=======interst=========\n")
    add_interst(5)

    # transaction filter:
    start_date = input("Enter the satrt date (YYYY-MM-DD) :")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    transaction_filter(start_date,end_date)

    # Final User Information
    display_user_info()
    print("-----------------------------\n")


if __name__ == "__main__":
    main()
    

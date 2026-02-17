from wallet_package.data import *
from wallet_package.auth import *
from wallet_package.profile import *
from datetime import datetime


def account_history():
    global user_transactions # [2323,345.6, 5567, 6757]
    # index = 1
    for index, (amt, timestamp) in enumerate(user_transactions):
        print(f" Transaction {index} : Amount {amt}, Date: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        

# account_history()

def transaction_filter(start_date,end_date):
    global user_transactions
    print(f"Get transactions from {start_date} to {end_date}")

    for amt, timestamp in user_transactions:
        if start_date <= timestamp <= end_date:
            print(f"Amount :{amt}, Date: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")


def debit_penalty(penalty):
    global wallet_balance,MINIMUM_BALANCE
    if(wallet_balance < MINIMUM_BALANCE):
        wallet_balance -= penalty
        print(" the wallet balance after penalty", wallet_balance)
    else:
        print(" No penalty- Balance:",wallet_balance)
# debit_penalty(50)

def add_interst(interst):
    global wallet_balance,is_active, MINIMUM_BALANCE
    print("Before intrest:", wallet_balance)
    
    if is_active and wallet_balance > MINIMUM_BALANCE and interst > 0:
        intrest_rate = interst/100
        intrest_amt = wallet_balance*intrest_rate
        wallet_balance +=intrest_amt
        print(" intrest amount:",intrest_amt)
        print("final balance:",wallet_balance)
    else:
        print("Cannot add intrest, check the balance")
    
# add_interst(5)

def transfer_funds(from_account, to_account, amount):
    print(f"transfering amount: {amount}, from: {from_account}, to: {to_account}")
    add_transaction(-amount)
    print(user_transactions)

# transfer_funds("shop_account","my_account",500)

calculate_fee = lambda amount: amount * 0.05

def check_validity(func):
    def validate(args,kwargs="credit"):
        if validate_transaction() and check_user_transaction():
            return func(args,kwargs)
        else:
            print("auth is failed")
    return validate
    

@check_validity
def add_transaction(new_transaction, type="credit"):
    global user_transactions, wallet_balance
    print("-------------------\n")
    
    fee = calculate_fee(new_transaction)
    if new_transaction < 10000:
        if type == "debit":
            total_amount = new_transaction +fee
            total_amount = - total_amount
        else:
            total_amount = new_transaction - fee
        print("the initial balance: ",wallet_balance)
        user_transactions_array.append(total_amount)
        user_transactions.append((total_amount, datetime.now() ))
        wallet_balance += total_amount
        print("updated balance: ", wallet_balance)
        print(f"the transaction fee is {fee}")
        print("the updated user transactions list: ",user_transactions)
        print("The user transactions array",user_transactions_array)
    else:
        print("user inactive or limit reached")
# add_transaction(300.0)

def sum_transactions(transactions, index=0):
    if index == len(transactions):
        return 0
    else:
        return transactions[index] + sum_transactions(transactions, index + 1)


def transaction_generator():
    global user_transactions
    for index, transaction in enumerate(user_transactions):
        message = yield transaction
        if message:
            print(f"message recieved: {message}")

# gen = transaction_generator()
# print(f"listof trans : {list(gen)}")
# print(f"first : {next(gen)}")
# print(gen.send("this is the message"))
# print(f"second: {next(gen)}")

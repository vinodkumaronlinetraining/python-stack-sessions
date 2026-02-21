from wallet_package.data import *
from wallet_package.auth import *
from wallet_package.profile import *
from wallet_package.log import *
from datetime import datetime


def account_history():
    global user_transactions # [2323,345.6, 5567, 6757]
    # index = 1
    try:
        if not user_transactions:
            raise ValueError("no transactions found")
        
        for index, (amt, timestamp) in enumerate(user_transactions):
            print(f" Transaction {index} : Amount {amt}, Date: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except NameError as e:
        print(f"NameError occured: {e}")
    except Exception as e:
        print(f"UnKnown Error : {e}")
    finally:
        print("the account_history function is attempted here")

# account_history()

def transaction_filter(start_date,end_date):
    global user_transactions
    print(f"Get transactions from {start_date} to {end_date}")
    try:
        if not user_transactions:
            raise ValueError("no transactions found")
        if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
            raise TypeError("start_date and end_date must be datetime objects")
        for amt, timestamp in user_transactions:
            if start_date <= timestamp <= end_date:
                print(f"Amount :{amt}, Date: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    except Exception as e:
        print(f"UnKnown Error : {e}")
    finally:
        print("the transaction_filter function is attempted here")

def debit_penalty(penalty):
    global wallet_balance,MINIMUM_BALANCE
    try:
        if(wallet_balance < MINIMUM_BALANCE):
            wallet_balance -= penalty
            print(" the wallet balance after penalty", wallet_balance)
        else:
            print(" No penalty- Balance:",wallet_balance)
    except TypeError as e:
        print(f"TypeError Caught: {e}")
    except Exception as e:
        print(f"UnKnown Error Caught: {e}")
    finally:
        print("the debit_penalty function is attempted here")
# debit_penalty(50)

def add_interst(interst):
    global wallet_balance,is_active, MINIMUM_BALANCE
    print("Before intrest:", wallet_balance)
    try:
        if is_active and wallet_balance > MINIMUM_BALANCE and interst > 0:
            intrest_rate = interst/100
            intrest_amt = wallet_balance*intrest_rate
            wallet_balance +=intrest_amt
            print(" intrest amount:",intrest_amt)
            print("final balance:",wallet_balance)
        else:
            print("Cannot add intrest, check the balance")
    except TypeError as e:
        print(f"TypeError Caught: {e}")
    except Exception as e:
        print(f"UnKnown Error Caught: {e}")
    finally:
        print("the add_interst function is attempted here")
# add_interst(5)

# def transfer_funds(from_account, to_account, amount):
#     print(f"transfering amount: {amount}, from: {from_account}, to: {to_account}")
#     add_transaction(-amount)
#     print(user_transactions)

# # transfer_funds("shop_account","my_account",500)

calculate_fee = lambda amount: amount * 0.05

def check_validity(func):
    def validate(args,kwargs="credit"):
        try:
            if validate_transaction() and check_user_transaction():
                return func(args,kwargs)
            else:
                print("auth is failed")
        except Exception as e:
            print(f"UnKnown Error Caught: {e}")
    return validate
    

@check_validity
def add_transaction(new_transaction, type="credit"):
    global user_transactions, wallet_balance
    print("-------------------\n")
    try:
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

            log_transaction(action=f"{type} Transaction", amount=total_amount)
        else:
            print("user inactive or limit reached")
            log_transaction(action="Transaction failed",amount=new_transaction )

    except TypeError as e:
        print(f"TypeError Caught: {e}")
        log_transaction(action="Type error occured, check the amount given", amount=new_transaction)
    except ValueError as e:
        print(f"ValueError Caught: {e}")
        log_transaction(action="Value error occured, check the amount given", amount=new_transaction)
    except Exception as e:
        print(f"UnKnown Error Caught: {e}")
        log_transaction(action="UnKonwn error occured", amount=new_transaction)
    finally:
        print("the add_transaction function is attempted here")
# add_transaction(300.0)

def sum_transactions(transactions, index=0):
    try:
        if index == len(transactions):
            return 0
        else:
            return transactions[index] + sum_transactions(transactions, index + 1)
    except TypeError as e:
        print(f"TypeError Caught: {e}")
    except Exception as e:
        print(f"UnKnown Error Caught: {e}")
    finally:
        print("the sum_transactions function is attempted here")


def transaction_generator():
    global user_transactions
    try:
        if not user_transactions:
            raise ValueError("no transactions found")
        for index, transaction in enumerate(user_transactions):
            message = yield transaction
            if message:
                print(f"message recieved: {message}")
    except ValueError as e:
        print(f"ValueError Caught: {e}")
    except Exception as e:
        print(f"UnKnown Error Caught: {e}")
    finally:
        print("the transaction_generator function is attempted here")
# gen = transaction_generator()
# print(f"listof trans : {list(gen)}")
# print(f"first : {next(gen)}")
# print(gen.send("this is the message"))
# print(f"second: {next(gen)}")



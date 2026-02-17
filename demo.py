user_transactions = [ 1000.0, 500.0, 345, 150.5, 400]
wallet_balance = 1000.0
MINIMUM_BALANCE, ALERT_BALANCE = 50, 100
is_active = True



# def check_validity(func):
#     def validate(*args,**kwargs):
#         if is_active:
#             print(" user is active, decorator is working")
#             return func(*args,**kwargs)
#         else:
#             print("auth is failed")
#     return validate

# def logger(function):
#     def log_transaction(*args, **kwprms):
#         print("this is a logger function")
#         return function(*args,**kwprms)
#     return log_transaction

# @check_validity
# @logger
# def add_transaction(*new_transactions, **keyword):
#     global user_transactions, wallet_balance
#     print("-------------------\n")

#     # if validate_transaction() and check_user_transaction():
#     for new_transaction in new_transactions:
#         if new_transaction < 10000:
#             print("the initial balance: ",wallet_balance)
#             user_transactions.append(new_transaction)
#             wallet_balance += new_transaction
#             print("updated balance: ", wallet_balance)
#             print("the updated user transactions list: ",user_transactions)
#             print(keyword)
#         else:
#             print("user inactive or limit reached")
# add_transaction(300.0,200,type="credit",id = "1234")



# # # combination of all the types args:
# # def add_transaction(new_transaction,type="debit", *extra_fees, **metadata):
# #     global user_transactions, wallet_balance

# #     if validate_transaction():
# #         total_amount = new_transaction + sum(extra_fees)
# #         if total_amount<10000:
# #             user_transactions.append(total_amount)
# #             wallet_balance += total_amount
# #             print(f"transaction type: {type}, amount:{total_amount}")
# #             print(f"Extra fees:{extra_fees}")
# #             print(f"Metadata: {metadata}")
# #         else:
# #             print("limit is reached")
# #     else:
# #         pass
# # add_transaction(200,"credit",10,5,6, description="ele_bill", id="R2345")


#                                                #  0,1,2,3,4,5
# # def sum_transactions(transactions, index=0):   # [1,2,3,4,5,6]
# #     if index == len(transactions): 
# #         return 0
# #     else:
# #         return transactions[index] + sum_transactions(transactions, index + 1)
    

# def transaction_range(): # [ 21,2,3,4,5]
#     global user_transactions

#     for i in range(len(user_transactions)): # range(5): [012345]
#         print(f"Transaction at index {i}: {user_transactions[i]}")

#     for i in range(1,4):
#         print(f"{user_transactions[i]}")

#     for i in range(-3,0):
#         print(f"{user_transactions[i]}")
    
# # transaction_range()

# calculate_area = lambda length,width: length*width

# # result = calculate_area(10,20)
# # print(result)

# def transaction_generator():
#     global user_transactions
#     for index, transaction in enumerate(user_transactions):
#         message =  yield f"Transaction{index}: {transaction}"
#         if message:
#             print(f"{message}")

# gen = transaction_generator()
# # print(list(gen))
# print(next(gen))
# print(f"the second:{next(gen)}")
# print(gen.send("this is the message"))

# exception handling
# -----------------

# 1. without exceptions seing what happens using different function calls

# def add_transaction(new_transaction):
#     global wallet_balance, user_transactions, is_active
#     amount = float(new_transaction)
#     if is_active and amount < 10000 and amount > 0:
#         user_transactions.append(amount)
#         wallet_balance += amount
#         print(f"Transaction successful: {amount}")
#     else:
#         print("Transaction failed: Invalid amount or account is inactive.")
    


# add_transaction(250.0)      # Success
# add_transaction(-100.0)     # Invalid amount
# add_transaction("invalid")  # TypeError
# add_transaction(None)       # TypeError

# 2. now using try, except blocks with general exception:

# def add_transaction(new_transaction):
#     global wallet_balance, user_transactions, is_active
#     try:
#         amount = float(new_transaction)
#         if is_active and amount < 10000 and amount > 0:
#             user_transactions.append(amount)
#             wallet_balance += amount
#             print(f"Transaction successful: {amount}")
#         else:
#             print("Transaction failed: Invalid amount or account is inactive.")
#     except Exception as e:
#         print("Invalid input: Please enter a numeric value for the transaction amount.", e)

# add_transaction(250.0)      # Success
# add_transaction(-100.0)     # Invalid amount
# add_transaction("invalid")  # TypeError
# add_transaction(None)       # TypeError


# 3. multiple builtin exceptions:

# def debit_penalty(penalty_amount):
#     try:
#         amount = float(penalty_amount)
#         if is_active and amount > 0 and amount < 5000:
#             global wallet_balance
#             wallet_balance -= amount
#             user_transactions.append(-amount)
#             print(f"Penalty deducted successfully: {amount}")
#             return wallet_balance
#         else:
#             raise ValueError("Penalty failed: invalid amount or account inactive")
#     except ValueError as e:
#         print(f"ValueError caught: {e}")
#     except TypeError:
#         print("TypeError caught: penalty amount must be a number")
#     except Exception as e:
#         print(f"Unexpected error caught: {e}")
#     finally:
#         print("Penalty processing completed.\n")

# debit_penalty(50.0)        # Success
# debit_penalty(-25.0)       # ValueError
# debit_penalty("invalid")   # ValueError
# debit_penalty(None)        # TypeError
# debit_penalty(10000.0)     # ValueError (exceeds limit)

# creating custom exceptions:
# ---------------------------------

class InValidAmountError(Exception):
    """this is a invalid amount error exception"""
    pass
class InActiveUserError(Exception):
     pass
def add_transcation(new_trans):
    global wallet_balance, user_transactions, is_active

    amount = float(new_trans)
    if not is_active:
         raise InActiveUserError("The user is inactive")
    if amount > 10000:
        raise InValidAmountError("The amount is above the limit ")
    if amount < 0:
        raise InValidAmountError("The amount is less than 0")
    
    user_transactions.append(amount)
    wallet_balance += amount
    print(f"Updated balance: {wallet_balance}")
    # print(f"this is the intrest: {intrest}")
    
        
       
    
try:

    add_transcation(100000)
except ValueError as e:
        print(f"ValueError Caught: {e}")
except InActiveUserError as e:
     print(f"InActiveusererror caught: {e}")
except InValidAmountError as e:
    print(f"invalidamounterror caught: {e}")
except NameError as e:
    print(f"NameError Caught: {e}")
except TypeError as e:
    print(f"TypeError Caught : {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivivsionError Caught: {e}")
except Exception as e:
        print(f"we have an error: {e}") 
finally:
     print("Add transaction function attempted")
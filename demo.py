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


def add_transactions(new):
    global wallet_balance, user_transactions, is_active
    try:
        amount = float(new)
        if is_active and amount < 10000 and amount > 0:
            user_transactions.append(amount)
            wallet_balance += amount
            print("transaction success")
        else:
            raise TypeError("invalid input")
    except Exception as e:
        print(f" Invalid input, transaction failed::::", e)    
add_transactions()

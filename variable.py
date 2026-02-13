# User Wallet Application:

# -----------------------
# initializing variables with proper naming conastraints
# -----------------------
application_name = "User App"
first_name = " VINOD "
last_name = "kumar"
address = 560064
password = 1234
wallet_balance = 1000.0
MINIMUM_BALANCE, ALERT_BALANCE = 50, 100
is_active = True

byte_password = password.to_bytes(2)
print(byte_password)
print(type(byte_password))

print(application_name, first_name, last_name, address, password, wallet_balance, is_active, sep=",")

def check_balance():
    if(wallet_balance <= ALERT_BALANCE):
        print(f"balance is low : {wallet_balance}")
    else:
        print(f"Your balance: {wallet_balance}")

check_balance()


# day 2
# -------------------------
# list datatype
user_transactions = [ 1000.0, 500.0, 345, 150.5, 400]
print(user_transactions)
print(type(user_transactions))

# tuple datatype
user_cred = ("8989","9090")
print(user_cred)
print(type(user_cred))

#list datatype
user_devices = {"my_phone", "my_pc","my_ipad","my_ipad"}
print(user_devices  )
print(type(user_devices))

# dictionary datatype:
user_profile = {
    "user_name": "vinod kumar",
    "address": 560064,
    "Wallet_balance": 1000.0
}
print(type(user_profile))

# function to change password: it also explains the use of global keyword
def change_password():
    global password
    password = input("Enter the new password:")
    print("changed password:",password)
change_password()
print("------------------------------------")


# type conversion: converting string data to float
string_password = float("8989")
print(string_password)
print(type(string_password))

# # add_transaction function: this shows how we validate a condition and add transactions
# ------------------------------------------------------------
# def add_transaction(new_transaction):
#     global user_transactions, wallet_balance
#     print("-------------------\n")

#     if validate_transaction() and check_user_transaction():
#         if new_transaction < 10000:
#             print("the initial balance: ",wallet_balance)
#             user_transactions.append(new_transaction)
#             wallet_balance += new_transaction
#             print("updated balance: ", wallet_balance)
#             print("the updated user transactions list: ",user_transactions)
#         else:
#             print("user inactive or limit reached")
# # add_transaction()


# change 1: changing add_transaction to have default parameters
-------------------------------------------------
# # this is an example of default parameters:
# def add_transaction(new_transaction, type="credit"):
#     global user_transactions, wallet_balance
#     print("-------------------\n")

#     # if validate_transaction() and check_user_transaction():
#     if new_transaction < 10000:
#         if type == "debit":
#             new_transaction = - new_transaction
#         print("the initial balance: ",wallet_balance)
#         user_transactions.append(new_transaction)
#         wallet_balance += new_transaction
#         print("updated balance: ", wallet_balance)
#         print("the updated user transactions list: ",user_transactions)
#     else:
#         print("user inactive or limit reached")
# add_transaction(300.0, "debit")


# change 2: changing add_transactions to show variable length arguements
# ----------------------------------------------------------
# this is called variable length args:

# def add_transaction(*new_transactions):
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
#         else:
#             print("user inactive or limit reached")
# add_transaction(300.0,400,500)

chnage 3: changing add_transaction to show all types of parameters
---------------------------------------------------------------
# combination of all the types args:
def add_transaction(new_transaction,type="debit", *extra_fees, **metadata):
    global user_transactions, wallet_balance

    if validate_transaction():
        total_amount = new_transaction + sum(extra_fees)
        if total_amount<10000:
            user_transactions.append(total_amount)
            wallet_balance += total_amount
            print(f"transaction type: {type}, amount:{total_amount}")
            print(f"Extra fees:{extra_fees}")
            print(f"Metadata: {metadata}")
        else:
            print("limit is reached")
    else:
        pass
add_transaction(200,"credit",10,5, description="ele_bill", id="R2345")
#------------------------------


# change 4: changing add_transaction to show decorator that adds description for a transaction
#---------------------------------------------------------
# def describe_transaction(function):
#     def content(new_transaction,type="credit",**metadata):
#         description = metadata.get("description","this i a dummy transaction")
#         print(f"processing transaction: {description}")
#         return function(new_transaction, type, **metadata)
#     return content

# @describe_transaction
# def add_transaction(new_transaction, type="credit",**metadata):
#     global user_transactions, wallet_balance
#     print("-------------------\n")

#     # if validate_transaction() and check_user_transaction():
#     if new_transaction < 10000:
#         if type == "debit":
#             new_transaction = - new_transaction
#         print("the initial balance: ",wallet_balance)
#         user_transactions.append(new_transaction)
#         wallet_balance += new_transaction
#         print("updated balance: ", wallet_balance)
#         print("the updated user transactions list: ",user_transactions)
#     else:
#         print("user inactive or limit reached")
# add_transaction(300.0,"debit")


#change 5: changing add_transaction to add a decorator that checks if user is valid, transaction is valid
#------------------------------------------------------
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
        user_transactions.append(total_amount)
        wallet_balance += total_amount
        print("updated balance: ", wallet_balance)
        print(f"the transaction fee is {fee}")
        print("the updated user transactions list: ",user_transactions)
    else:
        print("user inactive or limit reached")
# add_transaction(300.0)


# function to transfer funds from account1 to acc 2: positional args
#-----------------------------------------------------------------
def transfer_funds(from_account, to_account, amount):
    print(f"transfering amount: {amount}, from: {from_account}, to: {to_account}")
    add_transaction(-amount)
    print(user_transactions)

# transfer_funds("shop_account","my_account",500)


# function to debit penalty if wallet balance is below minimum balance:
#--------------------------------------------
def debit_penalty(penalty):
    global wallet_balance,MINIMUM_BALANCE
    if(wallet_balance < MINIMUM_BALANCE):
        wallet_balance -= penalty
        print(" the wallet balance after penalty", wallet_balance)
    else:
        print(" No penalty- Balance:",wallet_balance)
# debit_penalty(50)


# function to add intrest amount to the wallet balance:
#------------------------------------
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


# function to print all transactions one by one( using for loop, enumerate ):
#-----------------------------------------------------------------
def account_history():
    global user_transactions # [2323,345.6, 5567, 6757]
    # index = 1
    for index, data in enumerate(user_transactions):
        print(f" Transaction {index} : ",data)
        # index += 1

# account_history()


# function to print the sum of transactions ( showing recursive functions )
#---------------------------------------------------------
def sum_transactions(transactions, index=0):
    if index == len(transactions):
        return 0
    else:
        return transactions[index] + sum_transactions(transactions, index + 1)
    
# total_sum = sum_transactions(user_transactions) # [234,34,56,67]
# print(f"the sum of transactions is {total_sum}")


# function to print the no of transactions using range:
#--------------------------------------------------
def transaction_range():
    global user_transactions

    for i in range(len(user_transactions)):
        print(f"Transaction at index {i}: {user_transactions[i]}")

    for i in range(1,4):
        print(f"{user_transactions[i]}")

    for i in range(-3,0):
        print(f"{user_transactions[i]}")
    
transaction_range()


# lambda function to calculate an extra fee:
#---------------------------------
calculate_fee = lambda amount: amount + 50
fee = calculate_fee(500)


# empty function to be added later( shows use of pass )
#-------------------
def display_transactions_graph():
    pass


# function to check if user is active and transaction is valid:
#---------------------------------------------------
def validate_transaction():
    global is_active, wallet_balance, MINIMUM_BALANCE

    if is_active and wallet_balance > MINIMUM_BALANCE:
        # print("User is active, sufficient balance")
        return True, "User is active, sufficient balance"
    if is_active and wallet_balance <= MINIMUM_BALANCE:
        pass
    if not is_active and wallet_balance > MINIMUM_BALANCE:
        print("user is not active, but wallet balance is sufficient")
        return False
    else:
        print("user is not active and wallet_balance is low")
        return False
        
# result = validate_transaction()


# function to check user device and user pin:
#---------------------------------------------
def check_user_transaction():
    global user_cred, user_devices

    device_used = input("enter the device used:")
    pin_used = input("enter the trans pin: ")

    # if device_used in user_devices:
    #     print(f"{device_used} is valid")
    # else:
    #     print(f" the device {device_used} is invalid")

    # if pin_used in user_cred:
    #     print(f"{pin_used} is valid")
    # else:
    #     print(f"{pin_used} is not valid")
    if device_used in user_devices and pin_used in user_cred:
        print(f"valid user pin and trusted device{device_used}")
        return True
    else:
        print("user not trusted")
        return False
# check_user_transaction()


# function to check use of is, is not
#-------------------------------------
def check_device():
    global user_devices
                                                    
    user_device_1 = user_devices       
    user_device_2 = user_devices
    user_device_3 = list(user_devices) 

    if user_device_1 == user_device_2:
        print("they both refer to the same object")

    if user_device_1 is not user_device_3:
        print("they are not same")
    else:
        print(" they are same")
# check_device()


# function to add a new pin:( adding data to tuple )
#-------------------------
def add_pin(new_pin):
    global user_cred
    temp_list = list(user_cred)
    temp_list.append(new_pin)
    user_cred = tuple(temp_list)
    print(user_cred)
# add_pin("7878")


# function to print the elements of tuple seperately:( unpacking a tuple )
#----------------------------------------------------
def get_pins():
    transtn_pin = user_cred[0]
    print(transtn_pin)
# get_pins()


# function to update a dictionary by passing key and value:
#----------------------------------
def update_profile(key,value):
    print("initial data",user_profile)
    user_profile[key] = value
    print("updated profile",user_profile)
# update_profile(wallet_balance, 1500.0)


# function that shows variable length keyword arguements:
#--------------------------------------------------
# this is an example of variable length keyword args:
def update_profile(**kwargs):
    global user_profile

    for key, value in kwargs.items():
        user_profile[key]=value
        print(f"updated {key}: {value}")
    print("all the keyword args passed",kwargs)
    
# update_profile(address="90878",user_name= "vinod",  phone="90909090")


# function to display the user information accessing the dictionary:
#-------------------------------------------------------
def display_user_info():
    global first_name, last_name, user_profile, wallet_balance

    for key, value in user_profile.items():
        print(f"{key}: {value}")

# display_user_info()

# generator function that prints data from list when needed or asked using next keyword
#------------------------------------------------
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


# function to give user options and get the task
#-----------------------------------------------
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
            if new_trans <=0:
                print(" invalid input")
                continue
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

    # Final User Information
    display_user_info()
    print("-----------------------------\n")

if __name__ == "__main__":
    main()
    


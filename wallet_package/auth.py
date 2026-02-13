from wallet_package.data import * 
from wallet_package.transactions import *

user_devices = {"my_phone", "my_pc","my_ipad","my_ipad"}
user_cred = ("8989","9090")

def add_pin(new_pin):
    global user_cred
    temp_list = list(user_cred)
    temp_list.append(new_pin)
    user_cred = tuple(temp_list)
    print(user_cred)
# add_pin("7878")

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
# print(result)

def check_user_transaction():
    global user_cred, user_devices

    device_used = input("enter the device used:")
    pin_used = input("enter the trans pin: ")

    
    if device_used in user_devices and pin_used in user_cred:
        print(f"valid user pin and trusted device{device_used}")
        return True
    else:
        print("user not trusted")
        return False
# check_user_transaction()

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
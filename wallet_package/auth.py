from wallet_package.data import * 
from wallet_package.transactions import *
from wallet_package.exceptions import *

user_devices = {"my_phone", "my_pc","my_ipad","my_ipad"}
user_cred = ("8989","9090")



def add_pin(new_pin):
    global user_cred
    try:
        temp_list = list(user_cred)
        temp_list.append(new_pin)
        user_cred = tuple(temp_list)
        print(user_cred)
    except TypeError as e:
        print(f"Typeerror caught : {e}")
    except ValueError as e:
        print(f"ValueError Caught: {e}")
    except NameError as e:
        print(f"Nameerror Caught: {e}")
    except Exception as e:
        print(f"UnKnown error Caught: {e}")
    finally:
        print("The add_pin function is attempted")
# add_pin("7878")



def validate_transaction():
    global is_active, wallet_balance, MINIMUM_BALANCE
    try:
        if is_active and wallet_balance > MINIMUM_BALANCE:
            # print("User is active, sufficient balance")
            return True, "User is active, sufficient balance"
        if is_active and wallet_balance <= MINIMUM_BALANCE:
            raise LowBalanceError("The wallet_balance is below Min.")
        if not is_active and wallet_balance > MINIMUM_BALANCE:
            raise InActiveUserError("The user is inactive")
        else:
            raise InActiveUserError("The user is inactive and the wallet balance is also below min.")
    except LowBalanceError as e:
        print(f"LowBalanceError caught: {e}")
    except InActiveUserError as e:
        print(f"InActiveUserError caught: {e}")
    except Exception as e:
        print(f"UnKnownerror Caught: {e}")
    finally:
        print("The validate_transaction function is attempted here")
        
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
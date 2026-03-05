from wallet_package.data import * 
from wallet_package.transactions import *
from wallet_package.exceptions import *

class Auth:
    MINIMUM_BALANCE = 200
    ALERT_BALANCE = 500

    def __init__(self):
        self.user_devices = {"my_phone", "my_pc","my_ipad","my_ipad"}
        self.user_cred = ("8989","9090")



    def add_pin(self):
        
        try:
            new_pin = input("Enter the new pin:")
            if new_pin not in self.user_cred:
                if re.fullmatch(r'\d{4}',new_pin):
                    temp_list = list(self.user_cred)
                    temp_list.append(new_pin)
                    self.user_cred = tuple(temp_list)
                    print("Pin added")
                else:
                    raise ValueError("invalid pin format")
            else:
                raise ValueError("Pin already exists")
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



    def validate_transaction(self, wallet_balance, is_active):
        
        try:
            if is_active and wallet_balance > Auth.MINIMUM_BALANCE:
                # print("User is active, sufficient balance")
                return True, "User is active, sufficient balance"
            if is_active and wallet_balance <= Auth.MINIMUM_BALANCE:
                raise LowBalanceError("The wallet_balance is below Min.")
            if not is_active and wallet_balance > Auth.MINIMUM_BALANCE:
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

    def check_user_transaction(self):
        
        try:
            device_used = input("enter the device used:")
            pin_used = input("enter the trans pin: ")

            
            if device_used not in self.user_devices:
                raise InValidDeviceError(f"Device used {device_used} is not trusted")
            if pin_used not in self.user_cred:
                raise InValidPinError(f"Invalid Transaction pin entered")
            
            print(f"The device and pin verified")
            return True
        except InValidDeviceError as e:
            print(f"InValidDeviceError caught: {e}")
        except InValidPinError as e:
            print(f"InValidPinError Caught: {e}")
        except Exception as e:
            print(f"UnKnown error occured: {e}")
        finally:
            print("the check_user_transaction function is attempted")
    # check_user_transaction()


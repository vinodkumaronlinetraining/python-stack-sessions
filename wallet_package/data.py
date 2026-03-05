from datetime import datetime
from array import array
from wallet_package.exceptions import *
import re

class User:
    def  __init__(self, first_name, last_name, address, password):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.password = password
        self.wallet_balance = 1000.0
        self.is_active = True
        self.profile_info = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address
        }



    def change_password(self, new_password):
    
        try:
            if new_password and re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z@\d]{8,}$', new_password):

                self.password = new_password
                print("changed password:",self.password)
            else:
                raise Exception
        except ValueError as e:
            print(f"ValueError caught: {e}")
        except Exception as e:
            print(f"UnKnown Error Caught: {e}")
        finally:
            print("the change_password function is attempted here")


    def update_profile(self,key,value):
        
        try:
            if not isinstance(self.profile_info,dict):
                raise TypeError("user_profile must be a dictionary")
            
            self.profile_info[key]=value
            print(f"updated {key}: {value}")
            # print("all the keyword args passed",)
        
        except TypeError as e:
            print(f"TypeError Caught : {e}")
        except ValueError as e:
            print(f"ValueError Caught : {e}")
        except Exception as e:
            print(f"UnKnown Exception caught: {e}")
        finally:
            print("the update_profile function is attempted here")

    def display_info(self):
        print("User information")
        try:
            for key, value in self.profile_info.items():
                print(f"{key.capitalize()} : {value}")
            print(f"Wallet balance: {self.wallet_balance}")
        except Exception as e:
            print("Error Caught:", e)



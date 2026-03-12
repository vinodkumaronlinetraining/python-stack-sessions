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
        self.account_type = "Standard"
        self.profile_info = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address
        }

    def get_transaction_limit(self):  # original method
        return 10000                # this is the limit for standard account
    
    def get_fee_rate(self):  # original method
        return 0.02         # this is for the standard user

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

    def get_account_summary(self):
        print(f"[Standard Account] {self.first_name} {self.last_name}")
        print(f"Balance: Rs.{self.wallet_balance:.2f}")
        print(f" Status: { 'Active ' if self.is_active else 'Inactive'}")


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


class PremiumUser(User):
    def __init__(self, first_name, last_name, address, password):
        super().__init__(first_name, last_name, address, password)
        self.account_type = "Premium"
        self.cashback_balance = 0.0

    def get_transaction_limit(self):  # method overriding
        return 50000       # limit modified in the premium class method
    
    def get_fee_rate(self):  # method over riding
        return 0.01        # modified fee rate in the premium class method
    
    def add_cashback(self, amount):
        cashback = amount * 0.05
        self.cashback_balance += cashback

    def get_account_summary(self):   # over ridden
        print(f"[Premium Account] {self.first_name} {self.last_name}")
        print(f"Balance: Rs.{self.wallet_balance}")
        print(f" Cashback: {self.cashback_balance}")
        print(f" Status: {'Active' if self.is_active else 'Inactive'}")

    def display_info(self):
        super().display_info()
        print(f"Account_type: {self.account_type}")
        print(f"Cashback_balance: {self.cashback_balance}")
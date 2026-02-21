from wallet_package.data import *
import re

def change_password():
    global password
    try:
        new_password = input("Enter the new password:")
        if re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z@\d]{8,}$', new_password):

            password = new_password
            print("changed password:",password)
        else:
            raise Exception
    except ValueError as e:
        print(f"ValueError caught: {e}")
    except Exception as e:
        print(f"UnKnown Error Caught: {e}")
    finally:
        print("the change_password function is attempted here")
# change_password()

def display_user_info():
    global first_name, last_name, user_profile, wallet_balance
    try:
        if not user_profile:
            raise ValueError("user_profile is empty")
        for key, value in user_profile.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"ValueError caught: {e}")
    except Exception as e:
        print(f"UnKnown Exception caught: {e}")
    finally:
        print("the display_user_info function is attempted here")
# display_user_info()

def update_profile(**kwargs):
    global user_profile
    try:
        if not isinstance(user_profile,dict):
            raise TypeError("user_profile must be a dictionary")
        if not kwargs:
            raise ValueError("no data provided as arguements")
        
        for key, value in kwargs.items():
            user_profile[key]=value
            print(f"updated {key}: {value}")
        print("all the keyword args passed",kwargs)
    
    except TypeError as e:
        print(f"TypeError Caught : {e}")
    except ValueError as e:
        print(f"ValueError Caught : {e}")
    except Exception as e:
        print(f"UnKnown Exception caught: {e}")
    finally:
        print("the update_profile function is attempted here")
    
# update_profile(address="90878",user_name= "vinod",  phone="90909090")
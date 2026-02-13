from wallet_package.data import *


def change_password():
    global password
    password = input("Enter the new password:")
    print("changed password:",password)
# change_password()

def display_user_info():
    global first_name, last_name, user_profile, wallet_balance

    for key, value in user_profile.items():
        print(f"{key}: {value}")

# display_user_info()

def update_profile(**kwargs):
    global user_profile

    for key, value in kwargs.items():
        user_profile[key]=value
        print(f"updated {key}: {value}")
    print("all the keyword args passed",kwargs)
    
# update_profile(address="90878",user_name= "vinod",  phone="90909090")
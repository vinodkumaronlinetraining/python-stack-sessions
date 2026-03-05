transactions = [ 1000.0, 500.0, 345, -150.5, -400]
from datetime import datetime
wallet_balance = 1000.0
MINIMUM_BALANCE, ALERT_BALANCE = 50, 100
is_active = True
user_transactions = [(1000.0, datetime(2026, 1, 1, 10, 0)),
                     (500.0, datetime(2026, 2, 2, 9, 0)),
                     (346, datetime(2026, 2, 4, 5, 9)),
                     (500, datetime(2026, 5, 7, 7, 30)),
                     (-600, datetime(2026, 6, 6, 8, 40))
]


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

# class InValidAmountError(Exception):
#     """this is a invalid amount error exception"""
#     pass
# class InActiveUserError(Exception):
#      pass
# def add_transcation(new_trans):
#     global wallet_balance, user_transactions, is_active

#     amount = float(new_trans)
#     if not is_active:
#          raise InActiveUserError("The user is inactive")
#     if amount > 10000:
#         raise InValidAmountError("The amount is above the limit ")
#     if amount < 0:
#         raise InValidAmountError("The amount is less than 0")
    
#     user_transactions.append(amount)
#     wallet_balance += amount
#     print(f"Updated balance: {wallet_balance}")
#     # print(f"this is the intrest: {intrest}")
    
        
       
    
# try:

#     add_transcation(100000)
# except ValueError as e:
#         print(f"ValueError Caught: {e}")
# except InActiveUserError as e:
#      print(f"InActiveusererror caught: {e}")
# except InValidAmountError as e:
#     print(f"invalidamounterror caught: {e}")
# except NameError as e:
#     print(f"NameError Caught: {e}")
# except TypeError as e:
#     print(f"TypeError Caught : {e}")
# except ZeroDivisionError as e:
#     print(f"ZeroDivivsionError Caught: {e}")
# except Exception as e:
#         print(f"we have an error: {e}") 
# finally:
#      print("Add transaction function attempted")

# function to filter the transactions and create a new list

# def debit_transactions():
#     global user_transactions

#     for amt in user_transactions:
#         if amt < 0:
#             print(f"debit transactions: {amt}")

# debit_transactions()

# list comprehension:
# print(f"the user_transaction list: {user_transactions}")
# debit_transactions = [amt for amt in user_transactions if amt <0]
# print(debit_transactions)

# set comprehension:
user_devices = {"my_phone", "my_pc","my_ipad","my_ipad"}
# def add_device(new_device):
#     global user_devices

#     if new_device not in user_devices:
#         user_devices.add(new_device)
#         print("new device added",new_device)
# add_device("iphone")

# new_device = "iphone"
# user_devices = { device for device in user_devices if device != new_device} | {new_device}

# print(user_devices)

# print(user_transactions)
# transaction_summary = { amt: dt.strftime('%Y-%m-%d %H:%M:%S') for amt,dt in user_transactions}

# print("----------------\n")

# print(transaction_summary)


# open a new file
#---------------------
# file = open("sample.txt","w")
# file.write("this is a sample file")
# file.close()

# # read from an existing file:
# #---------------
# file = open("sample.txt","r")
# content = file.read()
# print(content)


# file = open("sample.txt","w")
# file.write("this is the second line in the file")
# file.close()

# file = open("sample.txt")
# content = file.read()
# print(content)

# file = open("sample.txt","a")
# file.write("\nthis is an additional append data")
# file.close


# file = open("sample.txt", "")
# content = file.readlines()
# print(content)

# import os
# os.remove("sample.txt")

# debit_trans = [ amt for (amt,timestamp) in user_transactions if amt < 0]
# print(debit_trans)


# user_devices = {"my_phone", "my_pc","my_ipad","my_ipad"}
# new_device = "computer1"
# user_devices = {device for device in user_devices if device != new_device} | {new_device}

# print(user_devices)

# text_file = open("sample.txt", 'w')
# text_file.write("This is a new file")
# text_file.close()

# text_file2 = open("sample.txt", 'w')
# data = text_file2.read()
# print(data)

# def save_transactions(filename,transaction):
#     global user_transactions

#     try:
#         with open(filename,'x') as file:
#             amt, timestamp = transaction
#             file.write(f"{amt}, {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
#         print("the append was successfull")

#     except Exception as e:
#         print("error caught: ",e)
# save_transactions("exclusive.txt",(250.0, datetime.now()))


# import json
# data = {
#     "name": "vinod",
#     "age": 30,
#     "city": "hyd"
# }
# file = open("sample.json", 'w')
# json.dump(data, file )


# f = open("sample.txt",'wb')
# data = " this is a binary data"
# f.write(data.encode("utf-8"))
# f.close()

# f = open("sample.txt", "r+")
# data = f.read()
# print(data)

import re

# pin = "rdse"
# if re.fullmatch(r'\d{4}', pin):
#     print("Valid pin")
# else:
#     print("Pattern doesnt match")


# email_id = "3@go.com"
# if re.fullmatch(r'^[\w\.]+@[\w\.]+\.\w+$', email_id):
#     print("valid email")
# else:
#     print("invalid email")

# password = "Vin12334"
# if re.fullmatch(r'^(?=.*[A-Z])(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
#     print("Password is valid")
# else:
#     print("invalid password")



# text = "please contact me at vi-n@gmail.com or vink@goo.in"
# # emails = re.findall(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', text)
# # print(emails)

# new_text = re.sub(r'\bcontact\b', 'text', text)
# print(new_text)


# class ClassName:
#     pass


# class MyClass:
#     greet = "Hello, All"   # atributes
#     id = ""

# # objects that are created for the class MyClass:
# english = MyClass()
# spanish = MyClass()

# # trying to access the attributes of the class using each object
# print(english.greet)
# print(spanish.greet)

# # trying to modify the attributes and creating own attributes
# spanish.greet = "Hola"
# print(spanish.greet)

# print(english.greet)
# english.greet = "hello everyone"

# # check the attributes related to each object
# print(english.__dict__)
# print(spanish.__dict__)

# english.id = "1234"
# print(english.id)

# class user with class attributes
# class User:
#     name = ""
#     email = ""
#     password = ""
# # each class contains attributes and methods

# # # create new objects
# user1 = User()
# user2 = User()

# user1.name = "vinod"
# user1.email = "vin@mail.com"
# user1.password = "12345678"

# print(user1.name)
# print(user1.email)
# print(user1.password)

# print(user2.name)
# print(user2.email)
# print(user2.password)

# print(user1.__dict__)
# print(user2.__dict__)


# class MyClass:
#     def greet(self,message):
#         print(message)

# english = MyClass()
# # MyClass.greet(english, "hello")
# english.greet("hello")
# spanish = MyClass()
# spanish.greet("hola")

# when ever we create an object of a class, python creates a default copy  of the object called instance
# whatever methods are there in the class accepts  the default object as the first parameter


# class Car:
#     def drive(self,brand,car_speed):
#         print(f"{brand} car is driving at speed:{car_speed}")

# car1 = Car()
# car2 = Car()

# car1.drive("Toyota",60)
# car2.drive("suzuki", 50)

# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def drive(self):
#         print(f"{self.brand} car is driving at speed:{self.speed}")

# car1 = Car("BMW", 100)
# car2 = Car("kia", 80)


# car1.drive()
# car2.drive()

# class Truck:
#     def __init__(self, wheels, brand):
#         self.wheels = wheels
#         self.brand = brand

#     def size(self):
#         print(f"the {self.brand} truck is of size with {self.wheels} wheels")

# vehicle1 = Truck(4,"Mahindra")
# vehicle2 = Truck(8, "Tata")

# __init__ method is the first method to be executed when we initialize an object, it is called by default. constructors

# difference with and without constructor:

# class User:
#     name = ""
#     email = ""
#     unique_id = ""


# user1 = User()

# user1.name = "vinod"
# user1.email = "vin@gmail.com"
# user1.unique_id = "emp1"

# print(user1.name)
# print(user1.email)
# print(user1.unique_id)

# user2 = User()

# user2.name = "vinod"
# user2.email = "vin@gmail.com"
# user2.unique_id = "emp1"

# print(user2.name)
# print(user2.email)
# print(user2.unique_id)


# when we use constructor:

# class User:
#     department = "software"

#     def __init__(self, name, email, unique_id):
#         self.name = name
#         self.email = email
#         self.unique_id = unique_id

# user1 = User("vinod", "vin@gmail.com", "emp01")

# user2 = User("ajay", "ajay@gmail.com", "emp02")

# print(user1.department)
# print(user1.name)
# print(user1.email)
# print(user1.unique_id)
# print("----------------------------------")
# user2.department = "Testing"
# print(user2.department)
# print(user2.name)
# print(user2.email)
# print(user2.unique_id)


# class House:
#     parking_spots = 2

#     def __init__(self,bedrooms, hall, kitchen):
#         self.bedrooms = bedrooms
#         self.hall = hall
#         self.kitchen = kitchen


#     def display_house(self):
#         print("Bedrooms", self.bedrooms)
#         print("halls", self.hall)
#         print("kitchens", self.kitchen)

# house1 = House(3,1,2)
# house2 = House(1,1,1)
# house3 = House(0,0,0)

# house1.display_house()
# print("---------------")
# house2.display_house()
# print("---------------")
# print("Parking spots",house1.parking_spots)

# class User:
#     def __init__(self,name,email): # (user1, vinod, vin@123.com)
#         self.name = name   # user1.name = vinod
#         self.email = email # user1.email = vin@123.com

#     def display(self): # user1
#         print(f"the name is {self.name}") # user1.name

# user1 = User("vinod", "vin@123.com")
# user2 = User("ajay", "aj@123.com")

# user1.display()




# class User:

#     def __init__(self, first_name, last_name, address, wallet_balance):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.address = address
#         self.wallet_balance = wallet_balance

#     def update_profile(self,first_name=None, last_name=None, address=None, wallet_balance=None):
#         if first_name:
#             self.first_name = first_name
#         if last_name:
#             self.last_name = last_name
#         if address:
#             self.address = address
#         if wallet_balance:
#             self.wallet_balance = wallet_balance

#         print("Profile updated")

#     def display_details(self):
#         print(f"First Name: {self.first_name}")
#         print(f"Last Name: {self.last_name}")
#         print(f"Address: {self.address}")
#         print(f"Wallet Balance: {self.wallet_balance}")

# # create different user objects:
# user1 = User("vinod", "Kumar", 560064, 1000.0)
# user2 = User("Vikram", "s", 546789, 500.9)

# user1.update_profile(address="hyd")
# user1.display_details()
# user2.display_details()


# 1. __init__ method:(constructor)

# class Dog:
#     def __init__(self,name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} barks!")

# d = Dog("Lab")
# d.bark()


# 2. class methods:

# class Dog:
#     total_dogs = 0

#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def get_count(cls,count):
#         cls.total_dogs = count
#         print(f"Total dogs: {cls.total_dogs}")

# d = Dog("rex")
# Dog.get_count(10)
# class Dog:
#     total_dogs = 0

#     def __init__(self, name):
#         self.name = name

#     # Regular instance method - receives 'self' (the instance)
#     def instance_method(self):
#         print(f"I am {self.name}, an instance")  # Can access instance data

#     # Class method - receives 'cls' (the class itself)
#     @classmethod
#     def class_method(cls):
#         cls.total_dogs += 1
#         print(f"Total dogs: {cls.total_dogs}")  # Operates on class-level data

#     # Without decorator - Python treats it as an instance method
    
#     def fake_class_method(cls):   # 'cls' is just a name, Python sees it as 'self'
#         print(type(cls))          # Will print the instance, NOT the class


# d1 = Dog("Rex")
# d2 = Dog("Max")

# # Instance method - needs an instance
# d1.instance_method()       # Works: "I am Rex, an instance"

# # Class method - can be called on CLASS or instance
# Dog.class_method()         # Works fine
# d1.class_method()          # Also works fine

# # Without @classmethod
# # Dog.fake_class_method()    # ERROR - Python passes no 'cls', so it's missing an arg
# d1.fake_class_method()     # "works" but cls is actually the instance d1, not the class



# 3. static method:

# class Math_opr:

#     def __init__(self, x,y):
#         self.x = x
#         self.y = y

#     @staticmethod    
#     def add(x,y):
#         print( x + y)
    
# result = Math_opr(5,10)
# result.add(20,30)


# double underscore methods or dunder methods:
# 1. __str__, __repr__

# class User:
#     def __init__(self, name): 
#         self.name = name

#     def __str__(self): # called whenever we use print statements with object
#         return f"User: {self.name}"
    
#     def __repr__(self): # called in interactive shell command interface whenever object name is used
#         return f"User(name='{self.name}')"
    
# user1 = User("Vinod")
# user2 = User("Manoj")
# print(user1)
# print(user2)
# user1    # print(repr(user1))


# 2. double underscore operator methods:

# class User:
#     def __init__(self,name):
#         self.name = name

#     def __repr__(self):          # ← add this
#         return f"User({self.name})"

#     def __add__(self, user_input):
#          return (User( self.name + user_input.name))

#     def __mul__(self, user_input):
#         return User( self.name * user_input )
    
#     def __len__(self):
#         return len(self.name)
    
#     def __eq__(self, user_input):
#         return self.name == user_input.name
    
#     def __lt__(self, user_input):
#         return self.name < user_input.name
    
#     def __gt__(self, user_input):
#         return self.name > user_input.name
    
# user1 = User("vinod")

# user2 = User("kumar")

# user3 = user1+ user2
# print(user3)
# # print(user1 > user2)


# 3. call method: executed whenever we call an object like a function

# class User:
#     def __init__(self, name):
#         self.name = name

#     def __call__(self):
#         print(f"User {self.name} is called as function")

# user1 = User("vinod")
# user1()

# 4. 

# class User:
#     def __init__(self, name):
#         self.name = name

#     def __getitem__(self, key):
#         return f" Accessing {key} of the user {self.name}"
    
#     def __setitem__(self, key, value):
#         print(f"Setting {key} to the value: {value}")

#     def __delitem__(self, key):
#         print(f"Deleting {key} of the user {self.name}")

#     def __iter__(self):
#         return iter([self.name])

    
# user1 = User([1,2,3,4,5])
# user2 = User("vikas")
# # print(user1["name"])

# # user1["address"] = "hyd"

# # del user1["name"]


# for name in user1:
#     print(name)


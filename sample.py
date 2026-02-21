# user_transactions = [ 1000.0, 500.0, 345, 150.5, 400]
# wallet_balance = 1000.0
# MINIMUM_BALANCE, ALERT_BALANCE = 50, 100
# is_active = True

# def add_transactions(new):
#     global wallet_balance, user_transactions, is_active
#     try:
#         amount = float(new)
#         if is_active and amount < 10000 and amount > 0:
#             user_transactions.append(amount)
#             wallet_balance += amount
#             print("transaction success")
#         else:
#             print("no") 
#     except Exception as e:
#         print(f" Invalid input, transaction failed::::", e)     
# add_transactions(10)

# Python regex:
#------------------------
# import re
# pin = "12360"

# if re.fullmatch(r'\d{5}', pin):
#     print(f"{pin} is valid")
# else:
#     print(f"error matching pin {pin}")

# import re
# email = "sample_89-co@_4.gmail.com"

# if re.fullmatch(r'^[\w\.-]+@[\w\.]+\.\w+$', email):
#     print(f"{email} is valid")
# else:
#     print(f"{email} not valid")


# import re

# password = "PAssword@123"
# # 1. cap letter, small, num, 8 len

# if re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z@\d]{8,}$', password):
#     print(f"{password} is valid")
# else:
#     print("error")


import re

# text  = "contact us at sample@gmil.com or sample@google.co.in for more info"
# emails = re.findall(r'\b[\w\.]+@[\w\.]+\.\w+\b', text)
# print(emails)

text = "contact us at sample@gmil.com or sample@gmil.com for more sample@gmil.com info"
new_text = re.sub(r'\bsample@gmil.com\b', 'abc.com', text)
print(new_text)
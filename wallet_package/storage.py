import json
from datetime import datetime
import os

class Storage:
    FILE_PATH = "users.json"

    @staticmethod
    def load_users():
        if os.path.exists(Storage.FILE_PATH):
            with open(Storage.FILE_PATH, 'r') as f:
                return json.load(f)
        return {}
    
    @staticmethod
    def save_user(user, transactions):
        try:
            data = Storage.load_users()
            data[user.first_name + "_" + user.last_name] = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "address": user.address,
                "password": user._password_for_storage,
                "wallet_balance": user.wallet_balance,
                "is_active": user.is_active,
                "account_type": user.account_type,
                "cashback_balance": getattr(user, "cashback_balance", 0.0),
                "transactions": [
                    {"amount": amt, "timestamp": ts.strftime('%Y-%m-%d %H:%M:%S')} for amt, ts in transactions
                ]
            }
            with open(Storage.FILE_PATH, 'w') as f:
                json.dump(data, f, )
            print("user data saved successfully")
        except Exception as e:
            print("Error caught:",e)

    @staticmethod    
    def load_user(first_name, last_name):
        try:
            data = Storage.load_users()
            key = first_name + "_" + last_name

            if key in data:
                record = data[key]
                transactions = [
                    (entry["amount"], datetime.strptime(entry["timestamp"], '%Y-%m-%d %H:%M:%S'))
                    for entry in record["transactions"]
                ]

                return record,transactions
        
            else:
                print("No record found for the user")
                return None, []
            
        except Exception as e:
            print("Error:",e)
            return None, []
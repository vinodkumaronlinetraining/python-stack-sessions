import json
from datetime import datetime
import os

class Storage:
    FILE_PATH = "users.json"

    @staticmethod
    def save_user(user, transactions):
        try:
            data = Storage._load_all() # loading the existing data
            data[user.first_name + "_" + user.last_name] = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "address": user.address,
                "password": user.password,
                "wallet_balance": user.wallet_balance,
                "is_active": user.is_active,
                "transactions": [{"amount": amt, "timestamp": ts.strftime('%Y-%m-%d %H:%M:%S')} for amt, ts in transactions
                ]
            }
            print("User data saved successfully")
        except Exception as e:
            print("Error:", e)

    @staticmethod
    def load_user(first_name, last_name):
        try:
            data = Storage._load_all()
            key = first_name + "_" + last_name

            if key in data:
                record = data[key]
                transactions = [
                    (entry["amount"], datetime.strptime(entry["timestamp"], '%Y-%m-%d %H:%M:%S'))
                    for entry in record["transactions"]
                ]
                return record, transactions
            else: 
                print("No data for this user")
                return None, []
        except Exception as e:
            print("Error:", e)
            return None, []
        
    @staticmethod
    def _load_all():
        if os.path.exists(Storage.FILE_PATH):
            with open(Storage.FILE_PATH, 'r') as f:
                return json.load(f)
            return {}
        
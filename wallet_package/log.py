import json
from datetime import datetime

def log_transaction(action, amount=None):
    log_entry = {
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "action": action,
        "amount": amount
    }
    try:
        with open('transaction_log.json', "a") as log_file:
            json.dump(log_entry, log_file)
            log_file.write('\n')
        print("Transaction log added successfully")
    except Exception as e:
        print("error caught: ",e)
        
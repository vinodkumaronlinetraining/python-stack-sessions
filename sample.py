user_transactions = [ 1000.0, 500.0, 345, 150.5, 400]
wallet_balance = 1000.0
MINIMUM_BALANCE, ALERT_BALANCE = 50, 100
is_active = True

def add_transactions(new):
    global wallet_balance, user_transactions, is_active
    try:
        amount = float(new)
        if is_active and amount < 10000 and amount > 0:
            user_transactions.append(amount)
            wallet_balance += amount
            print("transaction success")
        else:
            print("no") 
    except Exception as e:
        print(f" Invalid input, transaction failed::::", e)     
add_transactions(10)

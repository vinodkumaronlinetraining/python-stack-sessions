from datetime import datetime
from array import array
application_name = "User App"
first_name = " VINOD "
last_name = "kumar"
address = 560064
password = 1234
wallet_balance = 1000.0
MINIMUM_BALANCE, ALERT_BALANCE = 50, 100
is_active = True

user_profile = {
    "user_name": "vinod kumar",
    "address": 560064,
    "Wallet_balance": 1000.0
}

user_transactions_array = array("f",[1000.0, 500.0, 346.0, 500.0])

user_transactions = [(1000.0, datetime(2026, 1, 1, 10, 0)),
                     (500.0, datetime(2026, 2, 2, 9, 0)),
                     (346, datetime(2026, 2, 4, 5, 9)),
                     (500, datetime(2026, 5, 7, 7, 30))
]
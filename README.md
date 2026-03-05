# Wallet App — Session Summary

## What Was Covered Today

Today's session focused on refactoring the wallet app from a functional/module-based structure into a proper **Object-Oriented Programming (OOP)** design using classes, and then extending it with **JSON-based persistent storage**.

---

## 1. OOP Refactoring — Classes & Responsibilities

The app was reorganised into four classes, each with a single responsibility:

### `User` — `data.py`
Holds all user data and profile-related actions.

- **Attributes:** `first_name`, `last_name`, `address`, `password`, `wallet_balance`, `is_active`, `profile_info`
- **Methods:** `change_password()`, `update_profile()`, `display_info()`
- **Key fix:** `wallet_balance` was removed from `profile_info` dict to avoid stale data — `display_info()` now reads `self.wallet_balance` directly as the single source of truth

### `Auth` — `auth.py`
Handles all authentication and validation logic.

- **Attributes:** `user_cred`, `user_devices`, `MINIMUM_BALANCE`, `ALERT_BALANCE`
- **Methods:** `validate_user()`, `validate_transaction()`, `add_pin()`, `add_device()`

### `Wallet` — `transactions.py`
Processes transactions and manages transaction history.

- **Attributes:** `self.user`, `self.auth`, `self.user_transactions`
- **Methods:** `add_transaction()`, `access_transaction_history()`, `add_interest()`, `debit_penalty()`
- **Uses:** `@staticmethod` for `calculate_fee`, a custom `auth_required` decorator for validation

### `Logger` — `log.py`
Handles logging of all transaction events to a JSON file.

- **Method:** `log_transaction()` — static method that appends log entries to `transaction_log.json`

---

## 2. Key OOP Concepts Applied

### Dependency Injection
`Wallet.__init__` receives `user` and `auth` as parameters rather than creating them internally:

```python
def __init__(self, user, auth):
    self.user = user        # passed in — exists outside Wallet
    self.auth = auth        # passed in — exists outside Wallet
    self.user_transactions = []  # created internally — owned by Wallet
```

The rule: **pass in what already exists outside; create internally what only your class owns.**

### `auth_required` Decorator
A custom decorator inside `Wallet` that wraps transaction methods to enforce authentication before execution:

```python
def auth_required(func):
    def wrapper(self, *args, **kwargs):
        if not self.auth.validate_user() or not self.auth.validate_transaction(...):
            return False
        return func(self, *args, **kwargs)
    return wrapper
```

### Static Methods
`calculate_fee` is a `@staticmethod` — it's a utility that belongs to `Wallet` logically but needs no access to instance or class data:

```python
calculate_fee = staticmethod(lambda amount: amount * 0.02)
```

---

## 3. Persistent Storage — `storage.py`

A new `Storage` class was added to persist user data across sessions using a `users.json` file.

| Method | Purpose |
|---|---|
| `save_user(user, transactions)` | Saves/updates user data and transaction history to JSON |
| `load_user(first_name, last_name)` | Loads existing user data by name key |
| `_load_all()` | Internal helper to read the full JSON file |

**Storage format — `users.json`:**
```json
{
    "vinod_kumar": {
        "first_name": "vinod",
        "wallet_balance": 1500.0,
        "transactions": [
            {"amount": 490.0, "timestamp": "2025-01-01 10:00:00"}
        ]
    }
}
```

---

## 4. Bugs Fixed During Session

| Bug | Cause | Fix |
|---|---|---|
| `TypeError: Wallet.__init__() takes 1 argument but 2 given` | `__init__` was missing the `user` parameter | Added `user` and `auth` as parameters |
| `Wallet` calling `User()` internally | Treated `user` param as a class, not an object | Changed `self.user = User()` → `self.user = user` |
| `display_info` showing old balance | `profile_info` dict stored a copy of balance at creation time | Removed `wallet_balance` from dict, read `self.wallet_balance` directly |
| `update_profile` using positional arg | Called as `user1.update_profile(key, value)` but defined with `**kwargs` | Either fix the call or change method signature |

---

## 5. Module Structure

```
wallet_package/
│
├── data.py          → User class
├── auth.py          → Auth class
├── transactions.py  → Wallet class
├── log.py           → Logger class
├── storage.py       → Storage class (new)
└── exceptions.py    → Custom exceptions

main.py              → Entry point
users.json           → Persistent user data (auto-generated)
transaction_log.json → Transaction logs (auto-generated)
```
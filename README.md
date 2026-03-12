# Python Learning Series — Session 8
# Polymorphism, Method Overriding, Duck Typing & Overloading

---

## Table of Contents
1. [What is Polymorphism?](#1-what-is-polymorphism)
2. [Method Overriding](#2-method-overriding)
3. [Duck Typing](#3-duck-typing)
4. [Built-in Polymorphism](#4-built-in-polymorphism)
5. [Overloading in Python](#5-overloading-in-python)
6. [Polymorphism in the Wallet App](#6-polymorphism-in-the-wallet-app)
7. [Assessment 8 — Product App Tasks](#7-assessment-8--product-app-tasks)

---

## 1. What is Polymorphism?

**Polymorphism** means "many forms." It is the ability of different objects to respond to the **same method call** in their **own way**.

In Python, polymorphism is achieved through:
- **Method Overriding** — child class redefines a parent method
- **Duck Typing** — any object can be passed to a function as long as it has the expected method
- **Overloading** — same method behaves differently based on the arguments passed

### Why does it matter?
Without polymorphism, you would write separate functions for every type:
```python
# Without polymorphism — messy, hard to scale
def process_savings(account): ...
def process_current(account): ...
def process_loan(account):    ...

# With polymorphism — one function works for all
def process_month_end(account):
    account.apply_interest()   # each type handles it its own way
    account.apply_penalty()
```

---

## 2. Method Overriding

When a **child class** provides its own implementation of a method that already exists in the **parent class**, this is called **method overriding**.

The child's version **replaces** the parent's version for objects of that child class. You can still call the parent's version using `super()`.

### Example — Bank Accounts

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def apply_interest(self):
        print("No interest for base account")   # parent default

    def apply_penalty(self):
        print("No penalty for base account")    # parent default


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):                   # OVERRIDES parent
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest ₹{interest:.2f} added. New balance: ₹{self.balance:.2f}")

    def apply_penalty(self):                    # OVERRIDES parent
        print("Savings accounts have no penalty.")


class CurrentAccount(BankAccount):
    def apply_interest(self):                   # OVERRIDES parent
        print("Current accounts earn no interest.")

    def apply_penalty(self):                    # OVERRIDES parent
        penalty = 100
        self.balance -= penalty
        print(f"Penalty ₹{penalty} applied. New balance: ₹{self.balance:.2f}")


class LoanAccount(BankAccount):
    def __init__(self, owner, balance, loan_rate):
        super().__init__(owner, balance)
        self.loan_rate = loan_rate

    def apply_interest(self):                   # OVERRIDES parent — interest = more debt
        interest = self.balance * self.loan_rate
        self.balance += interest
        print(f"Loan interest ₹{interest:.2f} added. Outstanding: ₹{self.balance:.2f}")

    def apply_penalty(self):                    # OVERRIDES parent
        penalty = self.balance * 0.05
        self.balance += penalty
        print(f"Late penalty ₹{penalty:.2f} applied. Outstanding: ₹{self.balance:.2f}")
```

### Key Rules for Method Overriding
- The method name in the child **must match exactly** the parent's method name
- Use `super().method_name()` to call the parent's version first if you need it
- Python decides which version to run based on the **type of the object** at runtime

---

## 3. Duck Typing

> *"If it walks like a duck and quacks like a duck, it's a duck."*

Duck typing means Python **does not check the type** of an object — it only checks whether the object **has the method being called**. If it does, it works. If it doesn't, it raises an `AttributeError`.

### Example — Export Reports

```python
class PDF:
    def export(self):
        print("Exporting as PDF")

class Excel:
    def export(self):
        print("Exporting as Excel")

class CSV:
    def export(self):
        print("Exporting as CSV")

class Word:
    def save(self):             # different method name — NOT export()
        print("Saving Word doc")


def export_report(exporter):    # doesn't care about the type — only about .export()
    exporter.export()


export_report(PDF())            # ✅ works
export_report(Excel())          # ✅ works
export_report(CSV())            # ✅ works
export_report(Word())           # ❌ AttributeError — no export() method
```

### Example — Payment Processing

```python
class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")

class Crypto:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Bitcoin")


def process_payment(payment_method, amount):
    payment_method.pay(amount)      # works for any object that has pay()


process_payment(CreditCard(), 500)  # ✅
process_payment(UPI(), 500)         # ✅
process_payment(Crypto(), 500)      # ✅
```

### Duck Typing vs isinstance() check
```python
# Without duck typing — rigid, needs updating for every new class
def process_payment(method, amount):
    if isinstance(method, CreditCard):
        method.pay(amount)
    elif isinstance(method, UPI):
        method.pay(amount)
    # have to keep adding elif for every new payment type...

# With duck typing — flexible, works for any future class too
def process_payment(method, amount):
    method.pay(amount)   # just call it — if it has pay(), it works
```

---

## 4. Built-in Polymorphism

Python's own operators and functions already use polymorphism — the same symbol or function does different things depending on the type:

```python
# + operator behaves differently per type
print(10 + 20)              # 30          — arithmetic addition
print("hello" + " world")   # hello world — string concatenation
print([1, 2] + [3, 4])      # [1, 2, 3, 4] — list merge

# len() works on different types
print(len("hello"))         # 5  — characters in string
print(len([1, 2, 3]))       # 3  — items in list
print(len({1, 2, 3, 4}))    # 4  — items in set
```

This works because each type defines its own dunder methods (`__add__`, `__len__`, etc.) that Python calls automatically — which is itself a form of method overriding on built-in types.

---

## 5. Overloading in Python

**Overloading** means the same method behaves differently based on the **arguments passed to it**. Python achieves this using **default arguments** — the method adapts its behavior depending on what parameters are provided.

```python
class SavingsAccount(BankAccount):
    def apply_interest(self, months=1, compound=False):
        if compound:
            self.balance = self.balance * (1 + self.interest_rate) ** months
            print(f"Compound interest for {months} months. Balance: ₹{self.balance:.2f}")
        else:
            interest = self.balance * self.interest_rate * months
            self.balance += interest
            print(f"Simple interest for {months} months. Balance: ₹{self.balance:.2f}")


savings = SavingsAccount("Vinod", 10000, 0.05)

savings.apply_interest()           # default: simple, 1 month
savings.apply_interest(5)          # simple interest for 5 months
savings.apply_interest(6, True)    # compound interest for 6 months
```

### Overloading vs Overriding — Side-by-side

| | Overriding | Overloading |
|---|---|---|
| **Where** | Child class redefines parent's method | Same class, same method, different parameters |
| **How** | Different class, same method name | Same method, different arguments |
| **Python mechanism** | Inheritance + `super()` | Default arguments |
| **Example** | `SavingsAccount.apply_interest()` replaces `BankAccount.apply_interest()` | `apply_interest(months=1, compound=False)` adapts behavior per args |

---

## 6. Polymorphism in the Wallet App

### data.py — `PremiumUser` overrides `User`

```python
class User:
    def get_transaction_limit(self):
        return 10000           # Standard: ₹10,000 limit

    def get_fee_rate(self):
        return 0.02            # Standard: 2% fee

    def get_account_summary(self):
        print(f"[Standard Account] {self.first_name} {self.last_name}")
        print(f"  Balance: ₹{self.wallet_balance:.2f}")


class PremiumUser(User):
    def get_transaction_limit(self):
        return 50000           # Premium: ₹50,000 limit (OVERRIDES)

    def get_fee_rate(self):
        return 0.01            # Premium: 1% fee (OVERRIDES)

    def get_account_summary(self):                    # OVERRIDES parent
        print(f"[Premium Account] {self.first_name} {self.last_name}")
        print(f"  Balance : ₹{self.wallet_balance:.2f}")
        print(f"  Cashback: ₹{self.cashback_balance:.2f}")
```

### transactions.py — Duck Typing in `Wallet`

```python
class Wallet:
    def get_fee(self, amount):
        return self.calculate_fee(amount, self.user.get_fee_rate())
        # get_fee_rate() — Python calls the right version automatically
        # User → 2%,  PremiumUser → 1%

    def get_limit(self):
        return self.user.get_transaction_limit()
        # User → 10000,  PremiumUser → 50000
```

### main.py — Same function works for both wallet types

```python
def process_transaction(wallet):
    """Duck typing — works with both Wallet and PremiumWallet"""
    amount = input("Enter transaction amount: ")
    t_type = input("Enter transaction type (credit/debit): ")
    wallet.add_transaction(amount, t_type)   # correct behavior auto-selected
```



---


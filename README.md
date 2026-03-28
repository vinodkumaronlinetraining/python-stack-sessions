# Python OOP — Complete Concepts Summary

---

## 1. Classes & Objects

A **class** is a blueprint. An **object** is a real instance created from that blueprint.

```python
class MyClass:
    pass

obj = MyClass()   # creating an object
```

- Class names follow **CamelCase** convention
- `__dict__` shows the attributes of an object
- Multiple objects can be created from the same class, each with their own state

---

## 2. Attributes

**Class attributes** are shared by all instances. **Instance attributes** are unique to each object.

```python
class MyClass:
    greet = "Hello"        # class attribute — shared by all

obj1 = MyClass()
obj1.greet = "Hola"        # instance attribute — unique to obj1
```

---

## 3. The `__init__` Constructor

Automatically called when an object is created. Used to initialize instance attributes.

```python
class User:
    def __init__(self, name, email):
        self.name = name       # instance attribute
        self.email = email
```

**Why `self`?** When you call `obj.method()`, Python rewrites it as `Class.method(obj)` — automatically passing the instance as the first argument. `self` is just the conventional name for it.

```python
#Great question! Here's exactly why __init__ is needed over class attributes:
#The Problem with Class Attributes
class User:
    name = ""
    balance = 1000

user1 = User()
user2 = User()

user1.name = "Vinod"
user2.name = "Vikas"

print(user1.name)   # Vinod
print(user2.name)   # Vikas
Looks fine — but here's where it breaks:

class User:
    transactions = []    # ← class attribute (shared by ALL objects)

user1 = User()
user2 = User()

user1.transactions.append("₹500 credit")

print(user1.transactions)  # ['₹500 credit']
print(user2.transactions)  # ['₹500 credit'] ← user2 is affected too!
Both users share the same list — because class attributes are shared across all instances.
```

---

## 4. Types of Methods

### Instance Methods
Most common. Operate on a specific object's data. Take `self` as first parameter.

```python
def bark(self):
    print(f"{self.name} barks!")
```

### Class Methods (`@classmethod`)
Operate on the **class itself**. Receive `cls` automatically. Called on the class directly.

```python
@classmethod
def get_count(cls):
    print(f"Total: {cls.total}")
```

### Static Methods (`@staticmethod`)
Utility functions that belong to the class logically but need no access to instance or class data.

```python
@staticmethod
def validate_email(email):
    return "@" in email
```

| | Instance | Class Method | Static Method |
|---|---|---|---|
| First arg | `self` | `cls` | nothing |
| Access instance data | ✅ | ❌ | ❌ |
| Access class data | via `self.__class__` | ✅ | ❌ |
| Call on class directly | ❌ | ✅ | ✅ |

---
```python
class BankAccount:
    total_accounts = 0          # class attribute — shared by all
    MINIMUM_BALANCE = 500       # class attribute — same rule for everyone

    def __init__(self, owner, balance):
        self.owner = owner          # instance attribute — unique per object
        self.balance = balance      # instance attribute — unique per object
        BankAccount.total_accounts += 1

    # ─────────────────────────────────────────
    # INSTANCE METHODS
    # operate on a specific account's data
    # need self — tied to one particular object
    # ─────────────────────────────────────────

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"{self.owner} withdrew ₹{amount}. Balance: ₹{self.balance}")

    def display_info(self):
        print(f"Owner  : {self.owner}")
        print(f"Balance: ₹{self.balance}")

    # ─────────────────────────────────────────
    # CLASS METHOD
    # operates on the class itself, not one specific account
    # receives cls automatically — used for class-level data
    # ─────────────────────────────────────────

    @classmethod
    def get_total_accounts(cls):
        print(f"Total accounts opened: {cls.total_accounts}")

    @classmethod
    def set_minimum_balance(cls, amount):
        cls.MINIMUM_BALANCE = amount
        print(f"Minimum balance updated to ₹{cls.MINIMUM_BALANCE}")

    # ─────────────────────────────────────────
    # STATIC METHODS
    # utility functions related to BankAccount
    # no self or cls — don't need any object or class data
    # ─────────────────────────────────────────

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    @staticmethod
    def get_bank_info():
        print("Bank: ABC National Bank")
        print("Working Hours: Mon–Fri, 9AM–5PM")


# ─────────────────────────────────────────
# USAGE
# ─────────────────────────────────────────

acc1 = BankAccount("Vinod", 10000)
acc2 = BankAccount("Vikas", 20000)

# instance methods — called on a specific object
acc1.deposit(5000)          # only affects acc1
acc2.withdraw(3000)         # only affects acc2
acc1.display_info()

# class method — called on the class, not an object
BankAccount.get_total_accounts()       # Total accounts opened: 2
BankAccount.set_minimum_balance(1000)  # updates for ALL accounts

# static methods — called on the class, no object needed
BankAccount.get_bank_info()
print(BankAccount.validate_amount(500))   # True
print(BankAccount.validate_amount(-50))   # False

# also works on an object — but class/static methods don't use that object's data
acc1.get_total_accounts()    # still shows total — not just acc1's data
acc1.get_bank_info()         # same bank info regardless of which account calls it
```
### error situations: 
```python
# instance method needs self — can't call on class directly
BankAccount.deposit(500)          # ❌ missing self — which account's balance?

# class method only knows the class — can't touch instance data
@classmethod
def deposit(cls, amount):
    cls.balance += amount         # ❌ which account's balance? there are many!

# static method knows nothing — no self, no cls
@staticmethod
def deposit(amount):
    self.balance += amount        # ❌ self doesn't exist here
```

---

## One Line Summary for Each
```
instance method → "do something with THIS specific account's data"
class method    → "do something with ALL accounts / the account system"
static method   → "utility tool that belongs here but needs no account data"

## 5. Dunder / Magic Methods

Special methods with double underscores that define how objects behave with built-in operations.

### Representation
```python
def __str__(self):    # called by print() — for end users
def __repr__(self):   # called in console/debugging — for developers
```
> Always define `__repr__` at minimum — without it you get `<object at 0x...>`

### Operator Overloading
```python
def __add__(self, other):      # +   → always return, never print
def __sub__(self, other):      # -
def __mul__(self, other):      # *
def __truediv__(self, other):  # /
def __len__(self):             # len()
def __eq__(self, other):       # ==
def __lt__(self, other):       # <
def __gt__(self, other):       # >
```

### Other Useful Dunders
| Method | Triggered by |
|---|---|
| `__call__(self)` | `obj()` — calling object like a function |
| `__getitem__(self, key)` | `obj[key]` |
| `__setitem__(self, key, val)` | `obj[key] = val` |
| `__delitem__(self, key)` | `del obj[key]` |
| `__iter__(self)` | `for x in obj` |
| `__enter__` / `__exit__` | `with obj:` block |

---

```python
class User:
    def __init__(self, name):
        self.name = name
    
    def __str__(self): # called when the object is printed, used to define the string representation of the object
        return f"User: {self.name}"

    def __repr__(self): # called when the object is printed in the interactive shell, used to define the official string representation of the object
        return f"User(name='{self.name}')"

user1 = User("vinod")
print(user1)  # → User: vinod # this calls the __str__ method
user1  # → User(name='vinod') # this calls the __repr__ method


```
repr is used for debugging where we have detailed information, called when we user object name.
- str is used for end user, called when we print the object.

when we try to run the code in jupiter notebook or as shell comand
print(repr(user1))    it runs automatically this.

```python
class User:
    def __init__(self, name):
        self.name = name
    
    def __add__(self, other): # called when the + operator is used, used to define the behavior of the + operator for the class
        return User(self.name + " " + other.name)
    def __mul__(self, other): # called when the * operator is used, used to define the behavior of the * operator for the class
        return User(self.name * other)
    def __len__(self): # called when the len() function is used, used to define the behavior of the len() function for the class
        return len(self.name)
    def __eq__(self, other): # called when the == operator is used, used to define the behavior of the == operator for the class
        return self.name == other.name
    def __lt__(self, other): # called when the < operator is used, used to define the behavior of the < operator for the class
        return self.name < other.name
    def __gt__(self, other): # called when the > operator is used, used to define the behavior of the > operator for the class
        return self.name > other.name
user1 = User("vinod")
user2 = User("vikas")
user3 = user1 + user2 # this calls the __add__ method, it creates a new User object with the name "vinod vikas"
print(user3) # → User: vinod vikas # this calls the __str__ method of the new User object created by the __add__ method
print(len(user1)) # → 5 # this calls the __len__ method, it returns the length of the name attribute of user1
print(user1 == user2) # → False # this calls the __eq__ method, it compares the name attributes of user1 and user2
print(user1 < user2) # → True # this calls the __lt__ method, it compares the name attributes of user1 and user2
print(user1 > user2) # → False # this calls the __gt__ method, it compares the name attributes of user1 and user2
```

```python
class User:
    def __init__(self, name):
        self.name = name
    
    def __call__(self): # called when the object is called as a function, used to define the behavior of the object when it is called as a function
        print(f"User {self.name} called as a function!")
user1 = User("vinod")
user1() # → User vinod called as a function! # this calls the __call__ method, it prints a message when user1 is called as a function
```

```python
class User:
    def __init__(self, name):
        self.name = name
    
    def __getitem__(self, key): # called when the object is indexed, used to define the behavior of the object when it is indexed
        return f"Accessing {key} of user {self.name}"

    def __setitem__(self, key, value): # called when the object is indexed and assigned a value, used to define the behavior of the object when it is indexed and assigned a value
        print(f"Setting {key} of user {self.name} to {value}")

    def __delitem__(self, key): # called when the object is indexed and deleted, used to define the behavior of the object when it is indexed and deleted
        print(f"Deleting {key} of user {self.name}")

    def __iter__(self): # called when the object is iterated over, used to define the behavior of the object when it is iterated over
        return iter([self.name]) # this returns an iterator that iterates over a list containing the name attribute of the user

    def __next__(self): # called when the object is iterated over, used to define the behavior of the object when it is iterated over
        raise StopIteration # this raises a StopIteration exception to indicate that the iteration is complete
user1 = User("vinod")
print(user1["name"]) # → Accessing name of user vinod # this calls the __getitem__ method, it returns a message when user1 is indexed with "name"
user1["name"] = "vikas" # → Setting name of user vinod to vikas # this calls the __setitem__ method, it prints a message when user1 is indexed with "name" and assigned a value
del user1["name"] # → Deleting name of user vinod # this calls the __delitem__ method, it prints a message when user1 is indexed with "name" and deleted
for name in user1: # this calls the __iter__ method, it returns an iterator that iterates over a list containing the name attribute of user1
    print(name) # → vinod # this prints the name attribute of user1 during iteration
# when the iteration is complete, it calls the __next__ method, which raises a StopIteration exception to indicate that the iteration is complete
```

## 7. Inheritance

A child class inherits all attributes and methods of the parent class and can extend or override them.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls parent constructor
        self.breed = breed
```

**`super()`** calls the parent class method. Preferred over calling the parent by name directly as it handles multiple inheritance correctly.

### Types of Inheritance

**Single** — one child, one parent
```python
class Dog(Animal): pass
```

**Multiple** — one child, multiple parents
```python
class Child(Parent1, Parent2): pass
```

**Multilevel** — grandparent → parent → child chain
```python
class Child(Parent):      # Parent inherits from Grandparent
    pass
```

**Hierarchical** — multiple children from one parent
```python
class Dog(Animal): pass
class Cat(Animal): pass
```

**Hybrid** — combination of the above types

---

```python
# ─────────────────────────────────────────
# HYBRID INHERITANCE
# Single + Multiple + Multilevel combined
# ─────────────────────────────────────────

#        BankAccount          ← Base class
#        /         \
#  Savings        Current     ← Single inheritance (level 1)
#        \         /
#         Premium             ← Multiple inheritance (level 2)
#              |
#          VIPPremium         ← Multilevel inheritance (level 3)


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def display_info(self):
        print(f"Owner  : {self.owner}")
        print(f"Balance: ₹{self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest ₹{interest:.2f} added. Balance: ₹{self.balance:.2f}")


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance, overdraft_limit):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def apply_overdraft(self):
        print(f"Overdraft limit: ₹{self.overdraft_limit}")


class PremiumAccount(SavingsAccount, CurrentAccount):
    """inherits from BOTH Savings and Current — Multiple Inheritance"""
    def __init__(self, owner, balance, interest_rate, overdraft_limit):
        SavingsAccount.__init__(self, owner, balance, interest_rate)
        self.overdraft_limit = overdraft_limit
        self.cashback = 0.0

    def add_cashback(self, amount):
        self.cashback += amount * 0.05
        print(f"Cashback ₹{amount * 0.05:.2f} added. Total: ₹{self.cashback:.2f}")

    def display_info(self):
        super().display_info()
        print(f"Interest Rate  : {self.interest_rate * 100}%")
        print(f"Overdraft Limit: ₹{self.overdraft_limit}")
        print(f"Cashback       : ₹{self.cashback:.2f}")


class VIPPremiumAccount(PremiumAccount):
    """inherits from Premium — Multilevel Inheritance"""
    def __init__(self, owner, balance, interest_rate, overdraft_limit):
        super().__init__(owner, balance, interest_rate, overdraft_limit)
        self.concierge = True

    def display_info(self):
        super().display_info()
        print(f"Concierge      : {'Yes' if self.concierge else 'No'}")

    def book_concierge(self):
        print(f"Concierge service booked for {self.owner}")


# ─────────────────────────────────────────
# USAGE
# ─────────────────────────────────────────

print("========== Savings Account ==========")
savings = SavingsAccount("Vinod", 10000, 0.05)
savings.display_info()
savings.apply_interest()

print("\n========== Current Account ==========")
current = CurrentAccount("Vikas", 20000, 5000)
current.display_info()
current.apply_overdraft()

print("\n========== Premium Account ==========")
premium = PremiumAccount("Kiran", 50000, 0.07, 10000)
premium.display_info()
premium.apply_interest()    # from SavingsAccount
premium.apply_overdraft()   # from CurrentAccount
premium.add_cashback(2000)  # own method

print("\n========== VIP Premium Account ==========")
vip = VIPPremiumAccount("Raj", 100000, 0.10, 25000)
vip.display_info()
vip.apply_interest()        # from SavingsAccount (via Premium)
vip.apply_overdraft()       # from CurrentAccount (via Premium)
vip.add_cashback(5000)      # from PremiumAccount
vip.book_concierge()        # own method
```

---

## Output
```
========== Savings Account ==========
Owner  : Vinod
Balance: ₹10000
Interest ₹500.00 added. Balance: ₹10500.00

========== Current Account ==========
Owner  : Vikas
Balance: ₹20000
Overdraft limit: ₹5000

========== Premium Account ==========
Owner  : Kiran
Balance: ₹50000
Interest Rate  : 7.0%
Overdraft Limit: ₹10000
Cashback       : ₹0.00
Interest ₹3500.00 added. Balance: ₹53500.00
Overdraft limit: ₹10000
Cashback ₹100.00 added. Total: ₹100.00

========== VIP Premium Account ==========
Owner  : Raj
Balance: ₹100000
Interest Rate  : 10.0%
Overdraft Limit: ₹25000
Cashback       : ₹0.00
Concierge      : Yes
Interest ₹10000.00 added. Balance: ₹110000.00
Overdraft limit: ₹25000
Cashback ₹250.00 added. Total: ₹250.00
Concierge service booked for Raj
```

in case of multiple inheritance,
- we have 2 parents,
- super inherits which attributes?
- it follows Method resolution order(MRO).
- inherits first parent,
- manually define the attributes from second using self

---

## Inheritance Tree
```
        BankAccount
        /          \
  Savings         Current        ← Single inheritance
        \          /
          Premium                ← Multiple inheritance
              |
          VIPPremium             ← Multilevel inheritance
```

## 8. Polymorphism

The ability of different objects to respond to the same method call in their own way.

### Method Overriding
Child class provides its own implementation of a method defined in the parent.

```python
class BankAccount:
    def apply_interest(self):
        print("No interest")

class SavingsAccount(BankAccount):
    def apply_interest(self):        # overrides parent
        interest = self.balance * self.rate
        self.balance += interest
```

### Duck Typing
Python doesn't check the **type** of an object — only whether it has the method being called. *"If it walks like a duck and quacks like a duck, it's a duck."*

```python
def process_payment(payment_method, amount):
    payment_method.pay(amount)    # works for ANY object that has pay()

process_payment(CreditCard(), 500)   # ✅
process_payment(UPI(), 500)          # ✅
process_payment(Crypto(), 500)       # ✅
process_payment(InvalidObj(), 500)   # ❌ AttributeError — no pay() method
```

### Method Overloading (Python style)
Python doesn't support true overloading — instead, use **default parameters** to vary behavior based on what's passed:

```python
def apply_interest(self, months=1, compound=False):
    if compound:
        # compound interest logic
    else:
        # simple interest logic
```

### Built-in Polymorphism
Python's built-in operators already use polymorphism:
```python
10 + 20           # addition
"hello" + "world" # concatenation    — same operator, different behavior
[1,2] + [3,4]     # list merge

len("hello")      # 5
len([1,2,3])      # 3               — same function, different types
```

---

## 9. Key Takeaways

- **`__init__`** sets up each object's unique state at creation time
- **`self`** is automatically passed by Python — it's the instance calling the method
- **`@classmethod`** injects the class; without it Python treats it as an instance method
- **Always `return`** from `__add__` and other operator methods — never `print` inside them
- **Always define `__repr__`** so objects display meaningfully instead of memory addresses
- **Protected** (`_`) is a convention warning, not a real restriction — Python won't enforce it
- **Private** (`__`) is name-mangled and actually blocked outside the class
- **`super()`** is the correct way to call parent methods — flexible and future-proof
- **Duck typing** means Python trusts you — it won't verify types upfront, just tries to run

## 1. What is Encapsulation?

**Encapsulation** is the practice of:
- **Bundling** data (attributes) and the methods that operate on that data inside a single class
- **Restricting** direct access to some of that data from outside the class

Think of it like a capsule — the inner workings are protected. The only way to interact with the data is through the controlled methods the class exposes.

### Why does it matter?

| Without Encapsulation | With Encapsulation |
|---|---|
| Anyone can read or modify any attribute | Attributes are hidden behind controlled access |
| No validation on data changes | Setters can validate before accepting new values |
| Internal logic is exposed | Implementation details are hidden |
| Bugs from accidental modification | Data integrity is guaranteed |

---

## 2. The Problem Without Encapsulation

```python
class BankAccount:
    def __init__(self):
        self.balance = 1000.0

account = BankAccount()
account.balance = -99999    # ❌ nothing stops this — data corrupted
account.balance = "hello"   # ❌ wrong type — will break calculations later
```

There is no protection at all. Any code anywhere in the program can reach in and destroy the data. Encapsulation solves this.

---

## 3. Access Levels in Python

Python has three levels of access. They are enforced by **naming conventions**, not hard language rules (except for name mangling on private attributes).

```
public       →  self.name           no prefix     — accessible everywhere
protected    →  self._name          single _       — accessible in class + subclasses
private      →  self.__name         double __      — accessible only inside the class
```

```python
class BankAccount:
    def __init__(self):
        self.owner    = "Vinod"            # PUBLIC   — anyone can access
        self._phone   = "9876543210"       # PROTECTED — internal/subclass use
        self.__balance = 1000.0            # PRIVATE  — this class only

account = BankAccount()

print(account.owner)                       # ✅ Vinod
print(account._phone)                      # ⚠️  works but not recommended
print(account.__balance)                   # ❌ AttributeError
print(account._BankAccount__balance)       # ✅ 1000.0  (name-mangled access — for debugging only)
```

> **Important:** The single and double underscore are **conventions**, not hard restrictions. Python trusts developers to respect them. The double underscore triggers **name mangling** which makes accidental access harder but not impossible.

---

## 4. Private Attributes & Name Mangling

When you prefix an attribute with `__`, Python renames it internally to `_ClassName__attribute`. This is called **name mangling**.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 1000.0   # internally stored as _BankAccount__balance

account = BankAccount()

# Attempting direct access fails
account.__balance = -99999
print(account.__balance)         # prints -99999 — BUT this created a NEW attribute!
                                 # the original __balance is untouched

# Proof the real balance is safe
print(account._BankAccount__balance)   # 1000.0 — original is intact
```

### The right way — expose through public methods

```python
class BankAccount:
    def __init__(self):
        self.__balance = 1000.0

    def add_balance(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Amount must be positive.")

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.add_balance(500)
print(account.get_balance())     # 1500.0 — accessed safely through method
```

---

## 5. Protected Attributes & Methods

A single underscore `_` signals: *"This is internal — use with care. Don't access from outside unless you know what you're doing."*

Protected members **can** be accessed from subclasses — this is the key difference from private.

```python
class BankAccount:
    def __init__(self):
        self._balance       = 1000.0        # protected — subclasses may need this
        self._account_number = "1234567890"  # protected

    def _get_balance(self):                 # protected method
        return self._balance


class SavingsAccount(BankAccount):
    def apply_interest(self):
        interest = self._balance * 0.05     # ✅ subclass accessing protected attribute
        self._balance += interest
        print(f"Interest added. New balance: ₹{self._balance:.2f}")
```

---

## 6. Private Methods — Internal Logic Only

Private methods are helper functions that should only ever be called from **within the class**. They are prefixed with `__` and hidden from the outside world.

```python
class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner              = owner
        self._balance           = balance       # protected
        self.__pin              = pin           # private
        self.__transaction_log  = []            # private

    # PRIVATE — internal helper, not for outside use
    def __validate_pin(self, pin):
        return self.__pin == pin

    # PRIVATE — internal logging, outsiders shouldn't call this directly
    def __log_transaction(self, action, amount):
        self.__transaction_log.append({"action": action, "amount": amount})
        print(f"[LOG] {action}: ₹{amount}")

    # PUBLIC — the controlled way to deposit
    def deposit(self, amount, pin):
        if not self.__validate_pin(pin):        # calls private method internally
            print("Invalid PIN. Deposit failed.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._balance += amount
        self.__log_transaction("deposit", amount)
        print(f"Deposited ₹{amount}. New balance: ₹{self._balance}")

    # PUBLIC — controlled read access
    def get_balance(self, pin):
        if not self.__validate_pin(pin):
            print("Invalid PIN.")
            return None
        return self._balance

    # PUBLIC — controlled read access to log
    def get_transaction_log(self, pin):
        if not self.__validate_pin(pin):
            print("Invalid PIN.")
            return None
        return self.__transaction_log


account = BankAccount("Vinod", 1000, "1234")

# ✅ correct — through public methods only
account.deposit(500, "1234")          # Deposited ₹500. New balance: ₹1500
account.withdraw(200, "1234")         # Withdrew ₹200. New balance: ₹1300
print(account.get_balance("1234"))    # 1300

# ❌ private — direct access blocked
account.__validate_pin("1234")        # AttributeError
account.__pin                         # AttributeError
account.__log_transaction("x", 0)    # AttributeError
```



## 7. The @property Decorator

`@property` lets you define a method that behaves **like an attribute** when accessed, while still running validation logic behind the scenes. This is the Pythonic way to implement getters and setters.

```python
class Student:
    def __init__(self, name, marks):
        self.name      = name
        self.__marks   = marks       # private — controlled via property

    @property
    def marks(self):                 # GETTER — called when you read student.marks
        return self.__marks

    @marks.setter
    def marks(self, value):          # SETTER — called when you write student.marks = X
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Marks must be between 0 and 100.")


student = Student("Alice", 75)

print(student.marks)       # 75   ← calls getter, looks like attribute access
student.marks = 85         # ✅   ← calls setter, validation passes
print(student.marks)       # 85
student.marks = 150        # ❌   prints "Marks must be between 0 and 100."
print(student.marks)       # 85   ← unchanged because validation blocked it
```

### Without vs With @property

```python
# WITHOUT @property — two separate methods, awkward to call
student.set_marks(85)
print(student.get_marks())

# WITH @property — clean attribute-style access WITH hidden validation
student.marks = 85
print(student.marks)
```

### Three Parts of @property

```python
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):                 # 1. GETTER — defines how to read
        return self.__price

    @price.setter
    def price(self, value):          # 2. SETTER — defines how to write + validate
        if value >= 0:
            self.__price = value
        else:
            print("Price cannot be negative.")

    @price.deleter
    def price(self):                 # 3. DELETER — defines what happens on del
        print("Price deleted.")
        del self.__price
```

---

## 8. Read-Only Properties

If you define only the `@property` getter **without** a setter, the attribute becomes **read-only**. Any attempt to set it raises an `AttributeError`.

```python
class Employee:
    def __init__(self, name, salary):
        self.name       = name
        self.__salary   = salary

    @property
    def salary(self):
        return self.__salary     # getter only — no setter defined


employee = Employee("Bob", 50000)
print(employee.salary)           # ✅  50000
employee.salary = 60000          # ❌  AttributeError: can't set attribute
```

Use read-only properties when an attribute should be set once (in `__init__`) and never changed externally — for example an account number, order ID, or creation timestamp.

---

## 9. Full Reference — Access Level Summary

| Prefix | Level | Access from outside | Access from subclass | Access inside class |
|---|---|---|---|---|
| `name` | Public | ✅ Yes | ✅ Yes | ✅ Yes |
| `_name` | Protected | ⚠️ Possible (not recommended) | ✅ Yes | ✅ Yes |
| `__name` | Private | ❌ Blocked (name-mangled) | ❌ No | ✅ Yes |

### When to use each

| Scenario | Use |
|---|---|
| Normal data anyone can read or set | `self.name` — public |
| Internal data subclasses may need | `self._balance` — protected |
| Sensitive data (PIN, password, log) | `self.__pin` — private |
| Helper logic only this class uses | `def __validate()` — private method |
| Attribute that needs validation on set | `@property` with setter |
| Attribute that should never be changed | `@property` getter only (read-only) |

---

# DSA in Python — Summary

---

## Sorting Algorithms

| Algorithm | Best | Average | Worst | Space | Key Idea |
|-----------|------|---------|-------|-------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Swap adjacent elements repeatedly |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Insert each element into sorted position |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | Find minimum, swap to front |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Divide into halves, merge sorted halves |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | Pick pivot, partition around it |
| Tim Sort | O(n) | O(n log n) | O(n log n) | O(n) | Hybrid of merge + insertion sort |

> Tim Sort is Python's built-in sort — used by `sort()` and `sorted()`.

---

### Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

- Two nested loops → O(n²) time, O(1) space
- Best case O(n) when already sorted

---

### Insertion Sort

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

- Builds a sorted subarray from left to right
- Best case O(n) when array is nearly sorted

---

### Selection Sort

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

- Always O(n²) — no best case improvement
- Minimum swaps among O(n²) algorithms

---

### Merge Sort

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]; i += 1
            else:
                arr[k] = R[j]; j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]; i += 1; k += 1
        while j < len(R):
            arr[k] = R[j]; j += 1; k += 1
    return arr
```

- Stable sort — equal elements maintain original order
- O(n log n) always — no worst case degradation

---

### Quick Sort

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

- O(n²) worst case when pivot is always smallest/largest
- O(n log n) average — fastest in practice for in-memory sorting

---

### Tim Sort

```python
# Python uses Tim Sort internally
sorted_arr = sorted(arr)         # returns new sorted list
arr.sort()                       # sorts in place, returns None
arr.sort(reverse=True)           # descending order
arr.sort(key=lambda x: x[0])    # sort by custom key
```

- Hybrid: insertion sort for small runs + merge sort for combining
- Default algorithm in Python, Java, and Swift

---

## Searching Algorithms

| Algorithm | Time | Space | Requires Sorted? |
|-----------|------|-------|-----------------|
| Linear Search | O(n) | O(1) | No |
| Binary Search | O(log n) | O(1) | Yes |
| Jump Search | O(√n) | O(1) | Yes |
| Interpolation Search | O(log log n) avg | O(1) | Yes |
| Exponential Search | O(log n) | O(1) | Yes |
| Hash-based Search | O(1) avg | O(n) | No |

---

### Linear Search

```python
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
```

---

### Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

---

## Trees

A hierarchical data structure of nodes connected by edges.

### Key Terminology

| Term | Definition |
|------|-----------|
| Root | Topmost node, no parent |
| Parent / Child | Node with nodes below it / nodes below |
| Leaf | Node with no children |
| Edge | Link connecting parent to child |
| Depth | Distance from root to node |
| Height | Longest path from root to any leaf |

---

### Tree Node

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None
```

---

### Types of Trees

| Type | Rule | Use Case |
|------|------|----------|
| Binary Tree | At most 2 children per node | Expression parsing |
| BST | left < root < right | Fast lookup and insertion |
| AVL Tree | Self-balancing BST, height diff ≤ 1 | Databases |
| Heap | Parent ≥ children (max) or ≤ (min) | Priority queues |
| Trie | Each node = one character | Autocomplete |

---

### Binary Search Tree (BST)

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def search(self, target):
        return self._search(self.root, target)

    def _search(self, node, target):
        if node is None:
            return False
        if target == node.value:
            return True
        elif target < node.value:
            return self._search(node.left, target)
        else:
            return self._search(node.right, target)
```

- Search/Insert/Delete: O(log n) average, O(n) worst (skewed tree)
- Worst case occurs when inserting sorted values (1, 2, 3, 4...) — degrades to linked list

---

### Validate BST

```python
def is_valid_bst(root):
    def validate(node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (validate(node.left,  min_val,   node.value) and
                validate(node.right, node.value, max_val))
    return validate(root, float('-inf'), float('inf'))
```

> Key insight: pass down min/max bounds at each level. Going left tightens the upper bound; going right tightens the lower bound.

---

## Stack & Queue

### Stack — LIFO (Last In First Out)

```python
stack = []
stack.append(10)   # push  → [10]
stack.append(20)   # push  → [10, 20]
stack.append(30)   # push  → [10, 20, 30]
stack.pop()        # pop   → returns 30
stack[-1]          # peek  → 20
```

### Queue — FIFO (First In First Out)

```python
from collections import deque

queue = deque()
queue.append(10)    # enqueue → deque([10])
queue.append(20)    # enqueue → deque([10, 20])
queue.popleft()     # dequeue → returns 10
queue[0]            # peek    → 20
```

| | Stack | Queue |
|--|-------|-------|
| Order | LIFO | FIFO |
| Add | push (append) | enqueue (append) |
| Remove | pop | dequeue (popleft) |
| Real-life | Undo button, call stack | Ticket counter, printer |
| DSA use | DFS, recursion | BFS, scheduling |

---

## Graphs

A collection of nodes (vertices) connected by edges — no root, no hierarchy.

### Key Terminology

| Term | Definition |
|------|-----------|
| Vertex | A single node/entity |
| Edge | Connection between two vertices |
| Degree | Number of edges on a node |
| Weight | Cost assigned to an edge |
| Self-loop | Edge connecting node to itself |

---

### Types of Graphs

| Type | Description | Example |
|------|-------------|---------|
| Undirected | Edges have no direction — A—B same as B—A | Friendships |
| Directed | Edges have direction — A→B not same as B→A | Instagram follows |
| Weighted | Edges have a cost/distance | Road distances |
| Cyclic | Contains a cycle | Most social networks |
| Acyclic (DAG) | No cycles — directed | Task scheduling |
| Disconnected | Not all nodes reachable | Island networks |

---

### Representations

**Adjacency List** — O(V+E) space, preferred for sparse graphs

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B"],
    "F": ["C"]
}
```

**Adjacency Matrix** — O(V²) space, O(1) edge lookup

```python
#        A  B  C  D
matrix = [
    [0,  1,  1,  0],   # A
    [1,  0,  0,  1],   # B
    [1,  0,  0,  1],   # C
    [0,  1,  1,  0],   # D
]
```

| | Adjacency List | Adjacency Matrix |
|--|---------------|-----------------|
| Space | O(V + E) | O(V²) |
| Check edge | O(degree) | O(1) |
| Find neighbours | O(degree) | O(V) |
| Best for | Sparse graphs | Dense graphs |

---

### Graph Class

```python
class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u, v, weight=None):
        self.add_vertex(u)
        self.add_vertex(v)
        edge = (v, weight) if weight else v
        self.adj_list[u].append(edge)
        if not self.directed:
            edge2 = (u, weight) if weight else u
            self.adj_list[v].append(edge2)
```

---

## BFS — Breadth First Search

Explores level by level using a **queue**. Guarantees shortest path in unweighted graphs.

```python
from collections import deque

def bfs(graph, start, target):
    queue   = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(f"Visiting: {node}")

        if node == target:
            return True

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return False
```

**BFS on Trees — Level Order Traversal**

```python
def level_order(root):
    if not root:
        return []
    result = []
    queue  = deque([root])

    while queue:
        level_size = len(queue)    # freeze current level count
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)

    return result
```

- Time: O(V+E) for graphs, O(n) for trees
- Space: O(V) — queue holds at most one full level

---

## DFS — Depth First Search

Goes as deep as possible before backtracking, using a **stack** or recursion.

```python
def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(f"Visiting: {start}")

    if start == target:
        return True

    for neighbour in graph[start]:
        if neighbour not in visited:
            if dfs(graph, neighbour, target, visited):
                return True

    return False
```

**DFS on Trees**

```python
def dfs_tree(node, target):
    if node is None:
        return False

    print(f"Visiting: {node.value}")

    if node.value == target:
        return True

    if dfs_tree(node.left, target):
        return True

    print(f"Backtracking from: {node.value}")

    if dfs_tree(node.right, target):
        return True

    return False
```

### BFS vs DFS

| | BFS | DFS |
|--|-----|-----|
| Data structure | Queue | Stack / Recursion |
| Order | Level by level | Deep first |
| Shortest path | Yes (unweighted) | No |
| Space | O(w) — max width | O(h) — height |
| Use case | Shortest path, level traversal | Cycle detection, topological sort |

---

## Hash Map

Stores key-value pairs with O(1) average lookup, insert, delete.

### Creating a Hash Map

```python
# Method 1
person = {}
person["name"] = "Arjun"
person["age"]  = 25

# Method 2
person = {"name": "Arjun", "age": 25, "city": "Delhi"}

# Method 3
person = dict(name="Arjun", age=25, city="Delhi")
```

### Core Operations

```python
# read
print(person["name"])             # "Arjun"
print(person.get("salary", 0))    # 0 — safe read with default

# update / insert
person["age"] = 26
person["job"] = "Engineer"

# delete
del person["city"]
popped = person.pop("job")

# check key
if "name" in person:
    print("exists")

# iterate
for key, value in person.items():
    print(f"{key} → {value}")
```

### Time Complexity

| Operation | Average | Worst |
|-----------|---------|-------|
| Insert | O(1) | O(n) |
| Lookup | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Space | O(n) | O(n) |

> Worst case O(n) occurs when all keys hash to the same bucket (collision).

---

## Linked Lists

Nodes connected by pointers — not stored in contiguous memory.

### Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
```

---

### Doubly Linked List

```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
```

---

### Circular Linked List

```python
class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
```

---

### When to Use Which

| Type | Pointers | Direction | Use Case |
|------|----------|-----------|----------|
| Singly | `next` only | Forward only | Simple lists, stacks |
| Doubly | `next` + `prev` | Both ways | Browser history, undo/redo |
| Circular | `next` loops to head | Forward loop | Round-robin, playlists |

### Time Complexity

| Operation | Singly | Doubly | Circular |
|-----------|--------|--------|----------|
| Insert at head | O(1) | O(1) | O(1) |
| Insert at tail | O(n) | O(1)* | O(n) |
| Delete at head | O(1) | O(1) | O(1) |
| Search | O(n) | O(n) | O(n) |
| Access by index | O(n) | O(n) | O(n) |

*O(1) for doubly because tail pointer is maintained directly.

---

## Dynamic Programming

Solves problems by breaking them into overlapping subproblems and caching results to avoid recomputation.

### Two Approaches

**Top-down (Memoization)** — recursive + cache

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
```

**Bottom-up (Tabulation)** — iterative + table

```python
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

Both reduce Fibonacci from O(2ⁿ) naive recursion to **O(n) time, O(n) space**.

---

### Classic DP Problem — Climb Stairs

```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# climb_stairs(5) → 8
# Ways: [1+1+1+1+1, 1+1+1+2, 1+1+2+1, 1+2+1+1,
#        2+1+1+1, 1+2+2, 2+1+2, 2+2+1]
```

---

## Overall Complexity Cheatsheet

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Hash Map | O(1) | O(1) | O(1) | O(1) | O(n) |
| BFS / DFS | — | O(V+E) | — | — | O(V) |
| Graph (adj list) | — | O(V+E) | O(1) | O(E) | O(V+E) |

---

## Quick Decision Guide

| Use Case | Best Structure / Algorithm |
|----------|--------------------------|
| Fast lookup by key | Hash Map |
| Sorted data + fast search | BST (balanced) |
| Shortest path (unweighted) | BFS |
| Detect cycles, deep traversal | DFS |
| Frequent insert/delete at front | Linked List / Deque |
| Overlapping subproblems | Dynamic Programming |
| Large in-memory sort | Quick Sort / Tim Sort |
| Stable sort, linked list sort | Merge Sort |
| Nearly sorted data | Insertion Sort |
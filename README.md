# Wallet App — Session Summary

# Python Learning Series — Session 7
# Object-Oriented Programming: Inheritance & JSON Storage

---



## . JSON File Storage with a Storage Class

Instead of re-entering data every time the program runs, we can **persist data to a JSON file** and reload it on startup.

### Why JSON?
- Human-readable format
- Built-in Python support via the `json` module
- Easy to save and load dictionaries and lists
- Works well for storing structured data like user profiles and transactions



### Key Design Decisions
- `FILE_PATH` as a **class variable** means it's shared across all calls and easy to change in one place
- `_load_all()` is a **private static method** (prefixed with `_`) — it's a helper not meant to be called from outside the class
- The **first name + last name** combination is used as a unique dictionary key
- `datetime` objects are **serialized to strings** before saving (JSON cannot store datetime objects natively) and **parsed back** when loading
- All methods use `try/except` to handle file errors gracefully

---


### Flow Diagram

```
App Starts
    │
    ▼
Ask for name → Storage.load_user()
    │
    ├── Found → Restore User object + transactions from JSON
    │
    └── Not Found → Collect input → Create new User
    │
    ▼
Run menu loop
    │
    ▼
Choice == 'Save & Exit' → Storage.save_user() → Write to JSON → Exit
```

---


## 1. What is Inheritance?

Inheritance allows a **child class** to reuse the attributes and methods of a **parent class**, while also being able to add its own extra functionality.

### Why use Inheritance?
- Avoids repeating the same code across multiple classes (DRY — Don't Repeat Yourself)
- Models real-world relationships naturally (e.g., a `Student` **is a** `Learner`)
- Makes code easier to extend and maintain
- Child classes can override parent behaviour when needed

### Basic Syntax

```python
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Child inherits everything from Parent
class Student(Parent):
    pass

class Employee(Parent):
    pass

student1 = Student("Alice", 20)
employee1 = Employee("Bob", 30)

student1.display_info()   # Name: Alice, Age: 20
employee1.display_info()  # Name: Bob, Age: 30
```

> The child class name is followed by the parent class name in parentheses: `class Child(Parent)`

---

## 2. The `super()` Function

When a child class defines its own `__init__`, it needs to explicitly call the parent's `__init__` using `super()` to make sure the parent's attributes are still initialized.

```python
class Student(Learner):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)        # calls Learner's __init__
        self.student_id = student_id       # adds Student-specific attribute

    def display_student_info(self):
        self.display_info()                # calls inherited method
        print(f"Student ID: {self.student_id}")


class Employee(Learner):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee_info(self):
        self.display_info()
        print(f"Employee ID: {self.employee_id}")
```

### Key Points about `super()`
- `super().__init__()` calls the parent constructor — always include it when the child has its own `__init__`
- Without it, the parent's attributes (`name`, `age`) will not be initialized
- `super()` can also be used to call any parent method, not just `__init__`

---

## 3. Types of Inheritance

### 3.1 Single Inheritance
A child class inherits from **one** parent class. The most common and straightforward type.

```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def respond(self):
        print("Hello from Child")

c = Child()
c.greet()    # Hello from Parent
c.respond()  # Hello from Child
```

---

### 3.2 Multiple Inheritance
A child class inherits from **two or more** parent classes. The child gains access to all methods from all parents.

```python
class Parent1:
    def method1(self):
        print("Method from Parent1")

class Parent2:
    def method2(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):
    def method3(self):
        print("Method from Child")

child = Child()
child.method1()  # Method from Parent1
child.method2()  # Method from Parent2
child.method3()  # Method from Child
```

> **Note:** When two parent classes have a method with the same name, Python uses the **MRO (Method Resolution Order)** — left to right in the class definition — to decide which one runs.

---

### 3.3 Multilevel Inheritance
A class inherits from a parent, and then **another class inherits from that child**, forming a chain.

```python
class Grandparent:
    def method1(self):
        print("Method from Grandparent")

class Parent(Grandparent):
    def method2(self):
        print("Method from Parent")

class Child(Parent):
    def method3(self):
        print("Method from Child")

child = Child()
child.method1()  # Method from Grandparent  (inherited through chain)
child.method2()  # Method from Parent
child.method3()  # Method from Child
```

> Think of it as a **family tree**: grandchild inherits from parent who inherited from grandparent.

---

### 3.4 Hierarchical Inheritance
**Multiple child classes** all inherit from the **same single parent** class.

```python
class Parent:
    def method1(self):
        print("Method from Parent")

class Child1(Parent):
    def method2(self):
        print("Method from Child1")

class Child2(Parent):
    def method3(self):
        print("Method from Child2")

child1 = Child1()
child2 = Child2()

child1.method1()  # Method from Parent
child1.method2()  # Method from Child1

child2.method1()  # Method from Parent
child2.method3()  # Method from Child2
```

> Real-world analogy: `Car`, `Truck`, and `Bike` all inherit from a common `Vehicle` class.

---

### 3.5 Hybrid Inheritance
A **combination** of two or more types of inheritance in a single program.

```python
class Grandparent:
    def method1(self):
        print("Method from Grandparent")

class Parent1(Grandparent):
    def method2(self):
        print("Method from Parent1")

class Parent2(Grandparent):
    def method3(self):
        print("Method from Parent2")

class Child(Parent1, Parent2):     # multiple + multilevel combined
    def method4(self):
        print("Method from Child")

child = Child()
child.method1()  # Method from Grandparent
child.method2()  # Method from Parent1
child.method3()  # Method from Parent2
child.method4()  # Method from Child
```


---

### Summary Table: Inheritance Types

| Type | Description | Example |
|------|-------------|---------|
| Single | One child, one parent | `Student(Learner)` |
| Multiple | One child, many parents | `Child(Parent1, Parent2)` |
| Multilevel | Chain of inheritance | `Child → Parent → Grandparent` |
| Hierarchical | Many children, one parent | `Car, Truck, Bike(Vehicle)` |
| Hybrid | Mix of the above types | Combination of multiple + multilevel |

---
# ============================================================
#  10. OOP (Object Oriented Programming)
# ============================================================
# OOP organizes code into CLASSES (blueprints) and OBJECTS (instances).

# ----------------------------
# 1. Class & Object
# ----------------------------
class Dog:
    species = "Canis lupus"          # Class variable (shared by all)

    def __init__(self, name, age):   # Constructor
        self.name = name             # Instance variable (unique)
        self.age  = age

    def bark(self):                  # Instance method
        print(f"{self.name} says Woof!")

    def __str__(self):               # String representation
        return f"Dog({self.name}, {self.age})"

dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)
dog1.bark()
print(dog2)
print(Dog.species)

# ----------------------------
# 2. Inheritance
# ----------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Cat(Animal):                   # Cat inherits from Animal
    def speak(self):                 # Override parent method
        print(f"{self.name} says Meow!")

class Fish(Animal):
    pass                             # Uses parent's speak()

Cat("Whiskers").speak()              # Meow!
Fish("Nemo").speak()                 # makes a sound

# ----------------------------
# 3. super() — Call Parent Methods
# ----------------------------
class GuideDog(Dog):
    def __init__(self, name, age, owner):
        super().__init__(name, age)  # Call parent constructor
        self.owner = owner

    def guide(self):
        print(f"{self.name} guides {self.owner}")

gd = GuideDog("Rex", 4, "John")
gd.bark()                            # Inherited
gd.guide()                           # Own method

# ----------------------------
# 4. Encapsulation (Private Attributes)
# ----------------------------
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance     # __ makes it private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(f"Balance: {acc.get_balance()}")
# print(acc.__balance)              # ❌ ERROR — private!

# ----------------------------
# 5. Polymorphism
# ----------------------------
class Circle:
    def area(self): return 3.14 * 5 * 5

class Rectangle:
    def area(self): return 4 * 6

for shape in [Circle(), Rectangle()]:
    print(f"Area: {shape.area()}")   # Same method, different result

# ----------------------------
# 6. Class Methods & Static Methods
# ----------------------------
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):              # Uses class, not instance
        return cls.count

    @staticmethod
    def description():               # No access to class or instance
        return "I count instances"

c1, c2, c3 = Counter(), Counter(), Counter()
print(f"Total: {Counter.get_count()}")  # 3
print(Counter.description())

# ----------------------------
# 7. Magic / Dunder Methods
# ----------------------------
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):        # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):               # len(v)
        return int((self.x**2 + self.y**2)**0.5)

    def __repr__(self):              # repr(v) / print in list
        return f"Vector({self.x}, {self.y})"

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = v1 + v2
print(f"{v1} + {v2} = {v3}")
print(f"Length of v1: {len(v1)}")

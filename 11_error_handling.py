# ============================================================
#  11. ERROR HANDLING (Exceptions)
# ============================================================

# ----------------------------
# 1. try / except
# ----------------------------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ----------------------------
# 2. Catch the Exception Object
# ----------------------------
try:
    x = int("hello")
except ValueError as e:
    print(f"ValueError: {e}")

# ----------------------------
# 3. Multiple Exceptions
# ----------------------------
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Invalid types!")

safe_divide(10, 0)
safe_divide(10, "five")

# ----------------------------
# 4. else — Runs if NO exception
# ----------------------------
try:
    num = int("42")
except ValueError:
    print("Failed")
else:
    print(f"Success: {num}")

# ----------------------------
# 5. finally — ALWAYS runs
# ----------------------------
try:
    f = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleanup done (finally always runs)")

# ----------------------------
# 6. Common Exceptions
# ----------------------------
exceptions = {
    "ValueError"        : "Wrong value, e.g. int('abc')",
    "TypeError"         : "Wrong type for operation",
    "ZeroDivisionError" : "Division by zero",
    "IndexError"        : "List index out of range",
    "KeyError"          : "Missing dictionary key",
    "FileNotFoundError" : "File doesn't exist",
    "AttributeError"    : "Attribute doesn't exist",
    "NameError"         : "Variable not defined",
    "ImportError"       : "Module not found",
}
for exc, desc in exceptions.items():
    print(f"  {exc}: {desc}")

# ----------------------------
# 7. raise — Throw Your Own Exception
# ----------------------------
def set_age(age):
    if age < 0:
        raise ValueError(f"Age can't be negative! Got: {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Caught: {e}")

# ----------------------------
# 8. Custom Exceptions
# ----------------------------
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Can't withdraw {amount}. Balance: {balance}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(500, 1000)
except InsufficientFundsError as e:
    print(f"Custom Error: {e}")

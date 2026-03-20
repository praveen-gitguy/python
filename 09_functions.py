# ============================================================
#  09. FUNCTIONS
# ============================================================
# A function is a reusable block of code that runs when called.

# ----------------------------
# 1. Basic Function
# ----------------------------
def greet():
    """Docstring — describes what the function does."""
    print("Hello, World!")

greet()

# ----------------------------
# 2. Parameters & Return
# ----------------------------
def add(a, b):
    return a + b

result = add(3, 4)
print(f"3 + 4 = {result}")

# ----------------------------
# 3. Default Parameters
# ----------------------------
def greet_user(name, message="Welcome!"):
    print(f"{message} {name}")

greet_user("Praveen")                      # Uses default
greet_user("Alice", "Good morning,")       # Overrides default

# ----------------------------
# 4. Keyword Arguments
# ----------------------------
def describe(name, age, city):
    print(f"{name}, {age}, from {city}")

describe(age=25, city="Bangalore", name="Praveen")  # Order doesn't matter

# ----------------------------
# 5. *args — Variable Positional Arguments (Tuple)
# ----------------------------
def total(*numbers):
    print(f"Received: {numbers}")
    return sum(numbers)

print(total(1, 2, 3))
print(total(10, 20, 30, 40))

# ----------------------------
# 6. **kwargs — Variable Keyword Arguments (Dict)
# ----------------------------
def print_info(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")

print_info(name="Praveen", age=25, role="AI Engineer")

# ----------------------------
# 7. Combining Everything
# ----------------------------
def mixed(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

mixed("hello", 1, 2, 3, color="red", size=10)

# ----------------------------
# 8. Returning Multiple Values
# ----------------------------
def min_max(numbers):
    return min(numbers), max(numbers)  # Returns a tuple

low, high = min_max([3, 1, 8, 5, 2])
print(f"Min: {low}, Max: {high}")

# ----------------------------
# 9. Lambda (Anonymous Function)
# ----------------------------
double = lambda x: x * 2
add    = lambda a, b: a + b

print(double(5))                           # 10
print(add(3, 4))                           # 7

# Lambda with sorted
nums = [5, 2, 8, 1, 9]
desc = sorted(nums, key=lambda x: -x)
print(f"Descending: {desc}")

# ----------------------------
# 10. map() / filter() / reduce()
# ----------------------------
from functools import reduce

nums = [1, 2, 3, 4, 5]
doubled  = list(map(lambda x: x * 2, nums))       # Apply to each
evens    = list(filter(lambda x: x % 2 == 0, nums)) # Keep if True
total    = reduce(lambda a, b: a + b, nums)         # Accumulate

print(f"Doubled: {doubled}")
print(f"Evens: {evens}")
print(f"Total: {total}")

# ----------------------------
# 11. Scope — Local vs Global
# ----------------------------
count = 100                    # Global

def increment():
    global count               # Access global variable
    count += 1

increment()
print(f"Global count: {count}")  # 101

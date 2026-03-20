# ============================================================
#  VARIABLES & DATA TYPES
# ============================================================

# ----------------------------
# 1. Basic Data Types
# ----------------------------
name    = "Praveen"     # str   — text
age     = 25            # int   — whole number
height  = 5.9           # float — decimal number
is_cool = True          # bool  — True or False

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_cool))    # <class 'bool'>

# ----------------------------
# 2. Multiple Assignment
# ----------------------------
x = y = z = 0           # All set to 0
a, b, c = 1, 2, 3       # Assign multiple at once
print(f"x={x}, y={y}, z={z}")
print(f"a={a}, b={b}, c={c}")

# ----------------------------
# 3. Type Conversion (Casting)
# ----------------------------
num_str   = "100"
to_int    = int(num_str)        # str → int
to_float  = float(num_str)     # str → float
to_str    = str(42)             # int → str
to_bool   = bool(1)             # int → bool  (0=False, anything else=True)

print(f"'{num_str}' → int: {to_int}, float: {to_float}")
print(f"42 → str: '{to_str}', 1 → bool: {to_bool}")

# ----------------------------
# 4. Arithmetic Operators
# ----------------------------
a, b = 10, 3
print(f"Add        : {a + b}")    # 13
print(f"Subtract   : {a - b}")    # 7
print(f"Multiply   : {a * b}")    # 30
print(f"Divide     : {a / b}")    # 3.333...
print(f"Floor Div  : {a // b}")   # 3
print(f"Modulus    : {a % b}")    # 1
print(f"Power      : {a ** b}")   # 1000

# ----------------------------
# 5. Assignment Operators
# ----------------------------
x = 10
x += 5      # x = x + 5  → 15
x -= 3      # x = x - 3  → 12
x *= 2      # x = x * 2  → 24
x /= 4      # x = x / 4  → 6.0
x //= 2     # x = x // 2 → 3.0
x **= 3     # x = x ** 3 → 27.0
print(f"Final x: {x}")

# ----------------------------
# 6. input() — Taking User Input
# ----------------------------
# name = input("Enter your name: ")   # Always returns a str
# age  = int(input("Enter age: "))    # Convert to int for math
# print(f"Hello {name}, you are {age} years old!")

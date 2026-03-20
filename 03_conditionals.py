# ============================================================
#  CONDITIONALS (if / elif / else)
# ============================================================

# ----------------------------
# 1. Basic if / elif / else
# ----------------------------
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# ----------------------------
# 2. Comparison Operators
# ----------------------------
#   ==   equal to
#   !=   not equal to
#   >    greater than
#   <    less than
#   >=   greater than or equal to
#   <=   less than or equal to

print(10 == 10)     # True
print(10 != 5)      # True
print(10 > 20)      # False
print(5 <= 5)       # True

# ----------------------------
# 3. Logical Operators (and, or, not)
# ----------------------------
age = 20
has_id = True

if age >= 18 and has_id:
    print("Access granted")          # Both must be True

if age < 18 or has_id:
    print("Conditionally allowed")   # At least one True

if not False:
    print("not False is True")       # Inverts the value

# ----------------------------
# 4. Nested if
# ----------------------------
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Negative number")

# ----------------------------
# 5. Ternary Operator (One-line if)
# ----------------------------
x = 10
result = "even" if x % 2 == 0 else "odd"
print(f"{x} is {result}")

# ----------------------------
# 6. Membership Operators (in, not in)
# ----------------------------
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)           # True
print("mango" not in fruits)        # True

# ----------------------------
# 7. Identity Operators (is, is not)
# ----------------------------
a = [1, 2, 3]
b = a             # b points to SAME object as a
c = [1, 2, 3]     # c is a different object with same values

print(a is b)      # True  — same object in memory
print(a is c)      # False — different objects
print(a == c)      # True  — same values

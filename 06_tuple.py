# ============================================================
#  06. TUPLES
# ============================================================
# Ordered, IMMUTABLE (cannot change), Allows Duplicates
# Faster and more memory-efficient than lists

# ----------------------------
# 1. Creating
# ----------------------------
coordinates = (10, 20)
rgb_color   = (255, 128, 0)
mixed       = ("Alice", 30, True)
single      = (5,)                   # NEED trailing comma for 1 element
not_tuple   = (5)                    # This is just an int!
empty       = ()

print(type(single))                  # <class 'tuple'>
print(type(not_tuple))               # <class 'int'>

# ----------------------------
# 2. Indexing & Slicing
# ----------------------------
print(coordinates[0])                # 10
print(coordinates[-1])               # 20

nums = (1, 2, 3, 4, 5)
print(nums[1:4])                     # (2, 3, 4)
print(nums[::-1])                    # (5, 4, 3, 2, 1)

# ----------------------------
# 3. Immutability
# ----------------------------
try:
    coordinates[0] = 99              # ❌ ERROR
except TypeError as e:
    print(f"Error: {e}")

# ----------------------------
# 4. Packing & Unpacking
# ----------------------------
person = ("Praveen", 25, "Engineer")

# Unpacking into variables
name, age, job = person
print(f"Name: {name}, Age: {age}, Job: {job}")

# * captures remaining into a list
first, *rest = (1, 2, 3, 4, 5)
print(f"First: {first}, Rest: {rest}")   # Rest is a list

# ----------------------------
# 5. Tuple Methods (Only 2!)
# ----------------------------
colors = ("red", "blue", "red", "green", "red")
print(colors.count("red"))          # 3
print(colors.index("blue"))         # 1

# ----------------------------
# 6. Operations
# ----------------------------
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)                      # (1, 2, 3, 4, 5, 6)  concatenation
print(t1 * 3)                       # (1, 2, 3, 1, 2, 3, 1, 2, 3)  repetition
print(len(t1))                       # 3
print(2 in t1)                       # True

# Convert between list and tuple
as_list  = list(t1)
as_tuple = tuple(as_list)

# ----------------------------
# 7. When to Use Tuples?
# ----------------------------
# ✅ Data that should NEVER change (coordinates, dimensions)
# ✅ Returning multiple values from functions
# ✅ Dictionary keys (lists can't be dict keys, tuples can)
# ✅ Slightly faster than lists for read-only data

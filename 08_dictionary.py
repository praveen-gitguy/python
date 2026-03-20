# ============================================================
#  08. DICTIONARIES
# ============================================================
# Stores KEY : VALUE pairs
# Keys must be unique & immutable. Values can be anything.

# ----------------------------
# 1. Creating
# ----------------------------
person = {
    "name" : "Praveen",
    "age"  : 25,
    "city" : "Bangalore"
}
empty = {}

# ----------------------------
# 2. Accessing Values
# ----------------------------
print(person["name"])                 # Praveen (KeyError if missing!)
print(person.get("age"))             # 25
print(person.get("salary", "N/A"))   # N/A (safe — no error)

# ----------------------------
# 3. Adding & Updating
# ----------------------------
person["email"] = "praveen@mail.com" # Add new
person["age"]   = 26                 # Update existing
person.update({"city": "Mumbai", "job": "Engineer"})
print(person)

# ----------------------------
# 4. Removing
# ----------------------------
removed = person.pop("email")        # Remove & return value
del person["job"]                    # Delete key (no return)
last    = person.popitem()           # Remove last inserted pair
print(f"Popped: {removed}, Last: {last}")
print(person)

# ----------------------------
# 5. Checking Keys
# ----------------------------
print("name" in person)              # True
print("salary" in person)            # False

# ----------------------------
# 6. Looping
# ----------------------------
student = {"math": 90, "science": 85, "english": 78}

for key in student.keys():
    print(f"Subject: {key}")

for value in student.values():
    print(f"Score: {value}")

for key, value in student.items():
    print(f"{key}: {value}")

# ----------------------------
# 7. Methods
# ----------------------------
print(student.keys())                # dict_keys([...])
print(student.values())              # dict_values([...])
print(student.items())               # dict_items([...])

copy = student.copy()                # Shallow copy
student.clear()                      # Remove all
print(f"Cleared: {student}, Copy: {copy}")

# setdefault — return value if key exists, else insert with default
config = {"lr": 0.01}
config.setdefault("lr", 0.1)         # Won't change (key exists)
config.setdefault("epochs", 100)     # Adds epochs=100 (key missing)
print(config)

# fromkeys — create dict with same value for all keys
keys = ["a", "b", "c"]
print(dict.fromkeys(keys, 0))        # {'a': 0, 'b': 0, 'c': 0}

# ----------------------------
# 8. Nested Dictionaries
# ----------------------------
team = {
    "Alice": {"role": "ML Engineer", "exp": 3},
    "Bob"  : {"role": "Data Scientist", "exp": 5},
}
print(team["Alice"]["role"])          # ML Engineer

# ----------------------------
# 9. Dictionary Comprehension
# ----------------------------
squares = {x: x**2 for x in range(1, 6)}
print(squares)                        # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

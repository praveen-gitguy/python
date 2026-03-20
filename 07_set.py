# ============================================================
#  07. SETS
# ============================================================
# Unordered, Unindexed, UNIQUE values only

# ----------------------------
# 1. Creating
# ----------------------------
fruits  = {"apple", "banana", "cherry"}
dupes   = {1, 1, 2, 2, 3}            # Duplicates removed → {1, 2, 3}
empty   = set()                       # {} creates a dict, NOT a set!

print(dupes)
print(type(empty))

# ----------------------------
# 2. Adding Elements
# ----------------------------
fruits.add("orange")                  # Add one element
fruits.update(["mango", "kiwi"])      # Add multiple from any iterable
print(fruits)

# ----------------------------
# 3. Removing Elements
# ----------------------------
fruits.remove("banana")              # Remove — ERROR if not found
fruits.discard("pineapple")          # Remove — NO error if not found
popped = fruits.pop()                # Remove & return random element
print(f"Popped: {popped}, Remaining: {fruits}")

fruits2 = {"a", "b"}
fruits2.clear()                       # Remove all

# ----------------------------
# 4. Membership Check (Very Fast!)
# ----------------------------
animals = {"cat", "dog", "bird"}
print("cat" in animals)               # True
print("fish" not in animals)          # True

# ----------------------------
# 5. Set Operations
# ----------------------------
A = {"pen", "pencil", "notebook"}
B = {"notebook", "eraser", "pen"}

# Union — all elements combined
print(f"Union        : {A | B}")      # or A.union(B)

# Intersection — only common elements
print(f"Intersection : {A & B}")      # or A.intersection(B)

# Difference — in A but NOT in B
print(f"Difference   : {A - B}")      # or A.difference(B)

# Symmetric Difference — in A or B, but NOT both
print(f"Symm Diff    : {A ^ B}")      # or A.symmetric_difference(B)

# ----------------------------
# 6. Subset & Superset
# ----------------------------
X = {1, 2}
Y = {1, 2, 3, 4}
print(X.issubset(Y))                  # True  — X is inside Y
print(Y.issuperset(X))                # True  — Y contains X
print(X.isdisjoint({5, 6}))           # True  — no common elements

# ----------------------------
# 7. Practical: Remove Duplicates from a List
# ----------------------------
raw = ["cat", "dog", "cat", "bird", "dog"]
unique = list(set(raw))
print(f"Unique: {unique}")

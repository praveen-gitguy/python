# ============================================================
#  LISTS
# ============================================================
# Ordered, Mutable, Allows Duplicates

# ----------------------------
# 1. Creating
# ----------------------------
fruits  = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40, 50]
mixed   = ["hello", 42, True, 3.14]
empty   = []

# ----------------------------
# 2. Indexing
# ----------------------------
#         0        1         2
#      "apple", "banana", "cherry"
#        -3       -2        -1

print(fruits[0])      # apple  (first)
print(fruits[-1])     # cherry (last)

# ----------------------------
# 3. Slicing [start:stop:step]
# ----------------------------
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # [50, 40, 30, 20, 10]  (reversed)

# ----------------------------
# 4. Adding Elements
# ----------------------------
fruits.append("orange")            # Add to end
fruits.insert(1, "blueberry")      # Insert at index 1
fruits.extend(["mango", "kiwi"])   # Add all items from another list
print(f"After adding: {fruits}")

# ----------------------------
# 5. Removing Elements
# ----------------------------
fruits.remove("banana")       # Remove by value (first occurrence)
popped = fruits.pop()         # Remove & return last item
popped_at = fruits.pop(0)     # Remove & return item at index
del fruits[0]                 # Delete at index (no return)
print(f"After removing: {fruits}")

# ----------------------------
# 6. Useful Methods
# ----------------------------
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()                   # Sort ascending (modifies original)
print(f"Sorted: {nums}")

nums.sort(reverse=True)       # Sort descending
print(f"Sorted desc: {nums}")

nums.reverse()                # Reverse current order
print(f"Reversed: {nums}")

print(nums.index(5))          # Index of first occurrence
print(nums.count(1))          # Count occurrences
print(len(nums))              # Length

copy = nums.copy()            # Shallow copy
nums.clear()                  # Remove all elements
print(f"Cleared: {nums}, Copy: {copy}")

# ----------------------------
# 7. List Comprehension
# ----------------------------
# [expression for item in iterable if condition]
squares = [x**2 for x in range(1, 6)]
evens   = [x for x in range(20) if x % 2 == 0]
labels  = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]

print(f"Squares: {squares}")         # [1, 4, 9, 16, 25]
print(f"Evens: {evens}")             # [0, 2, 4, ...]
print(f"Labels: {labels}")           # ['Odd', 'Even', ...]

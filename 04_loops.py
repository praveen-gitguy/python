# ============================================================
#  LOOPS (for, while)
# ============================================================

# ----------------------------
# 1. for Loop — Iterate over a sequence
# ----------------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop over a string
for char in "Python":
    print(char, end=" ")
print()

# ----------------------------
# 2. range(start, stop, step)
# ----------------------------
for i in range(5):               # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(2, 7):            # 2, 3, 4, 5, 6
    print(i, end=" ")
print()

for i in range(0, 20, 5):        # 0, 5, 10, 15
    print(i, end=" ")
print()

for i in range(5, 0, -1):        # 5, 4, 3, 2, 1 (countdown)
    print(i, end=" ")
print()

# ----------------------------
# 3. while Loop — Runs while condition is True
# ----------------------------
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1                    # MUST update to avoid infinite loop

# ----------------------------
# 4. break — Exit the loop early
# ----------------------------
for i in range(1, 10):
    if i == 5:
        print("Breaking at 5")
        break
    print(i)

# ----------------------------
# 5. continue — Skip current iteration
# ----------------------------
for i in range(1, 8):
    if i == 4:
        continue                  # Skip 4
    print(i, end=" ")
print()

# ----------------------------
# 6. else with Loops
# ----------------------------
# else runs ONLY if the loop finishes WITHOUT a break
for i in range(3):
    print(i, end=" ")
else:
    print("— Loop completed!")

for i in range(5):
    if i == 3:
        break
else:
    print("This won't print — break was hit")

# ----------------------------
# 7. enumerate() — Loop with index
# ----------------------------
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

for index, color in enumerate(colors, start=1):  # Start from 1
    print(f"{index}: {color}")

# ----------------------------
# 8. zip() — Loop over multiple lists together
# ----------------------------
names  = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ----------------------------
# 9. Nested Loops
# ----------------------------
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

# ----------------------------
# 10. Multiplication Table (Practical Example)
# ----------------------------
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# ============================================================
#  12. FILE HANDLING
# ============================================================

import os

# ----------------------------
# 1. Writing to a File ("w" — overwrites)
# ----------------------------
with open("/tmp/sample.txt", "w") as f:
    f.write("Line 1: Hello World\n")
    f.write("Line 2: Python is great\n")
    f.write("Line 3: File handling is easy\n")
print("File written.")

# ----------------------------
# 2. Reading a File ("r")
# ----------------------------
# Read entire file
with open("/tmp/sample.txt", "r") as f:
    content = f.read()
print(content)

# Read line by line
with open("/tmp/sample.txt", "r") as f:
    for line in f:
        print(f">> {line.strip()}")

# Read all lines into a list
with open("/tmp/sample.txt", "r") as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")

# ----------------------------
# 3. Appending ("a" — adds to end)
# ----------------------------
with open("/tmp/sample.txt", "a") as f:
    f.write("Line 4: Appended line\n")
print("Appended.")

# ----------------------------
# 4. File Modes Summary
# ----------------------------
# "r"  — read only (error if no file)
# "w"  — write (creates/overwrites)
# "a"  — append (creates if needed)
# "r+" — read and write
# "rb" — read binary (images, PDFs)
# "wb" — write binary

# ----------------------------
# 5. Working with Paths (os module)
# ----------------------------
print(f"Exists : {os.path.exists('/tmp/sample.txt')}")
print(f"Is file: {os.path.isfile('/tmp/sample.txt')}")
print(f"Size   : {os.path.getsize('/tmp/sample.txt')} bytes")

# ----------------------------
# 6. CSV Files
# ----------------------------
import csv

# Write CSV
with open("/tmp/data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score", "grade"])
    writer.writerow(["Alice", 92, "A"])
    writer.writerow(["Bob", 75, "B"])
    writer.writerow(["Carol", 88, "A"])

# Read CSV
with open("/tmp/data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row['name']}: {row['score']} ({row['grade']})")

# ----------------------------
# 7. JSON Files
# ----------------------------
import json

# Write JSON
config = {"model": "ResNet", "lr": 0.001, "epochs": 50}
with open("/tmp/config.json", "w") as f:
    json.dump(config, f, indent=4)

# Read JSON
with open("/tmp/config.json", "r") as f:
    loaded = json.load(f)
print(f"Model: {loaded['model']}, LR: {loaded['lr']}")

# ----------------------------
# 8. Cleanup
# ----------------------------
for f in ["/tmp/sample.txt", "/tmp/data.csv", "/tmp/config.json"]:
    if os.path.exists(f):
        os.remove(f)
print("Cleanup done.")

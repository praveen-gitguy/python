# ============================================================
#  STRINGS
# ============================================================

# ----------------------------
# 1. Creating Strings
# ----------------------------
s1 = 'Hello'                       # Single quotes
s2 = "World"                       # Double quotes
s3 = """This is a
multi-line string"""               # Triple quotes
print(s1, s2)
print(s3)

# ----------------------------
# 2. Indexing & Slicing
# ----------------------------
text = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5
#      -6 -5 -4 -3 -2 -1

print(text[0])          # P       (first)
print(text[-1])         # n       (last)
print(text[0:3])        # Pyt     (index 0, 1, 2)
print(text[::2])        # Pto     (every 2nd char)
print(text[::-1])       # nohtyP  (reversed)

# ----------------------------
# 3. String Concatenation & Repetition
# ----------------------------
greeting = "Hello" + " " + "World"    # Concatenation
line     = "-" * 30                   # Repetition
print(greeting)
print(line)

# ----------------------------
# 4. String Formatting (3 Ways)
# ----------------------------
name, age = "Praveen", 25

# f-strings (Recommended ✅)
print(f"Name: {name}, Age: {age}")

# .format()
print("Name: {}, Age: {}".format(name, age))

# % operator (Old-style)
print("Name: %s, Age: %d" % (name, age))

# ----------------------------
# 5. Case Methods
# ----------------------------
msg = "hello, Python World"
print(msg.upper())          # HELLO, PYTHON WORLD
print(msg.lower())          # hello, python world
print(msg.title())          # Hello, Python World
print(msg.capitalize())     # Hello, python world
print(msg.swapcase())       # HELLO, pYTHON wORLD

# ----------------------------
# 6. Search & Replace
# ----------------------------
text = "I love Python programming"
print(text.find("Python"))           # 7  (index where found, -1 if not)
print(text.count("o"))               # 2  (number of occurrences)
print(text.replace("Python", "AI"))  # I love AI programming
print(text.startswith("I love"))     # True
print(text.endswith("ing"))          # True

# ----------------------------
# 7. Strip (Remove Whitespace)
# ----------------------------
padded = "   Hello   "
print(f"'{padded.strip()}'")      # 'Hello'         (both sides)
print(f"'{padded.lstrip()}'")     # 'Hello   '      (left only)
print(f"'{padded.rstrip()}'")     # '   Hello'      (right only)

# ----------------------------
# 8. Split & Join
# ----------------------------
csv_line = "apple,banana,cherry"
parts = csv_line.split(",")          # → ['apple', 'banana', 'cherry']
print(parts)

rejoined = " | ".join(parts)         # → 'apple | banana | cherry'
print(rejoined)

# ----------------------------
# 9. Checking Content
# ----------------------------
print("123".isdigit())      # True  — all digits
print("abc".isalpha())      # True  — all letters
print("abc123".isalnum())   # True  — letters or digits
print("   ".isspace())      # True  — only whitespace

# ----------------------------
# 10. Escape Characters
# ----------------------------
print("Line1\nLine2")       # \n → new line
print("Col1\tCol2")         # \t → tab
print("She said \"Hi\"")    # \" → literal quote
print("Path: C:\\folder")   # \\ → literal backslash

# ----------------------------
# 11. Strings are IMMUTABLE
# ----------------------------
s = "hello"
# s[0] = "H"               # ❌ ERROR — cannot modify in place
s = "H" + s[1:]             # ✅ Create a new string
print(s)                    # Hello

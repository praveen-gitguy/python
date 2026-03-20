# ============================================================
#  14. MODULES & PACKAGES (pip)
# ============================================================
# A MODULE is a single .py file with reusable code.
# A PACKAGE is a folder of modules (installed via pip).

# ----------------------------
# 1. Importing Built-in Modules
# ----------------------------
import math
print(math.sqrt(16))             # 4.0
print(math.pi)                   # 3.14159...
print(math.ceil(4.2))            # 5
print(math.floor(4.8))           # 4

import random
print(random.randint(1, 100))    # Random int between 1-100
print(random.choice(["a", "b", "c"]))  # Random pick

import datetime
now = datetime.datetime.now()
print(f"Current time: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")

import os
print(f"Current directory: {os.getcwd()}")

# ----------------------------
# 2. Import Styles
# ----------------------------
import math                      # Import entire module
from math import sqrt, pi       # Import specific items
from math import *               # Import everything (avoid this!)
import math as m                 # Alias — m.sqrt(16)
from math import sqrt as s       # Alias — s(16)

print(sqrt(25))                  # 5.0 (imported directly)
print(m.pi)                      # 3.14... (via alias)

# ----------------------------
# 3. Creating Your Own Module
# ----------------------------
# File: helpers.py
#   def greet(name):
#       return f"Hello, {name}!"
#
# File: main.py
#   from helpers import greet
#   print(greet("Praveen"))

# ----------------------------
# 4. __name__ == "__main__"
# ----------------------------
# This check ensures code only runs when the file is executed directly,
# NOT when it's imported as a module.

def main():
    print("This runs only when executed directly.")

if __name__ == "__main__":
    main()

# ----------------------------
# 5. Installing Packages with pip (Run in Terminal)
# ----------------------------
#   pip install numpy              Install a package
#   pip install numpy==1.24.0      Install specific version
#   pip install numpy pandas       Install multiple at once
#   pip uninstall numpy            Remove a package
#   pip list                       Show all installed packages
#   pip show numpy                 Show details of a package
#   pip freeze                     List packages with versions
#   pip freeze > requirements.txt  Save to file
#   pip install -r requirements.txt Install from file

# ----------------------------
# 6. Popular Packages for ML/AI
# ----------------------------
packages = {
    "numpy"       : "Matrix math, arrays, tensors",
    "pandas"      : "Data manipulation (CSV, Excel, DataFrames)",
    "matplotlib"  : "Data visualization (charts, graphs)",
    "seaborn"     : "Statistical data visualization",
    "scikit-learn": "Classical ML (regression, classification, clustering)",
    "tensorflow"  : "Deep learning framework (Google)",
    "pytorch"     : "Deep learning framework (Meta)",
    "opencv-python": "Computer vision (image processing)",
    "nltk"        : "Natural language processing",
    "flask"       : "Web framework (for deploying ML models as APIs)",
    "requests"    : "HTTP requests (calling APIs)",
    "jupyter"     : "Interactive notebooks for experimentation",
}

print("\n📦 Key Packages for ML/AI:")
for pkg, desc in packages.items():
    print(f"  {pkg:16s} — {desc}")

# ----------------------------
# 7. Quick Start for ML
# ----------------------------
# Run these in terminal (inside a virtual environment):
#
#   pip install numpy pandas matplotlib scikit-learn jupyter
#
# Then launch Jupyter Notebook:
#   jupyter notebook

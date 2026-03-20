# 13. Virtual Environments & Package Management

A virtual environment is an **isolated Python setup**.  
Each project gets its own packages — no conflicts!

> **Why?**  
> Project A needs `numpy 1.24`, Project B needs `numpy 2.0`.  
> Without a venv, they'd clash. With a venv, each has its own.

---

## Traditional Way (pip + venv)

### 1. Create a Virtual Environment

```bash
python3 -m venv .venv
```

This creates a `.venv` folder with its own Python. Common names: `venv`, `.venv`, `env`.

### 2. Activate

```bash
# Mac / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

After activation your terminal shows: `(.venv) $`  
Now any `pip install` goes into this environment only.

### 3. Deactivate

```bash
deactivate
```

### 4. Install Packages

```bash
pip install numpy                  # Install a package
pip install numpy pandas           # Install multiple
pip install "numpy>=1.24"          # With version constraint
pip uninstall numpy                # Remove
pip list                           # Show all installed
pip show numpy                     # Details of one package
```

### 5. Save & Restore Packages

```bash
pip freeze > requirements.txt      # Save installed packages to file
pip install -r requirements.txt    # Install everything from file
```

### 6. Best Practice for Projects

```bash
mkdir my_project
cd my_project
python3 -m venv .venv
source .venv/bin/activate
pip install numpy pandas
pip freeze > requirements.txt
```

> **⚠️ .gitignore** — Never commit the venv folder!  
> Add `.venv/` to your `.gitignore`. Only commit `requirements.txt`.

---

## Modern Way — uv (Recommended 🚀)

`uv` is a **blazing-fast** Python package manager written in Rust.  
Made by **Astral** (creators of the Ruff linter).  
It replaces: `pip`, `pip-tools`, `virtualenv`, and `pyenv` — **all in one tool**.

### Why uv?

- ✅ **10-100x faster** than pip
- ✅ Handles **venv + packages + Python versions** in one tool
- ✅ Built-in **lockfile** support (reproducible builds)
- ✅ Works with existing `requirements.txt`

### 7. Install uv

```bash
# Mac / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip
pip install uv
```

### 8. uv — Virtual Environments

```bash
uv venv                           # Create .venv (default)
uv venv myenv                     # Custom name
source .venv/bin/activate          # Activate (same as before)
deactivate                         # Deactivate (same as before)
```

### 9. uv — Installing Packages

```bash
uv pip install numpy               # Install a package
uv pip install numpy pandas        # Install multiple
uv pip install "numpy>=1.24"       # With version constraint
uv pip uninstall numpy             # Remove
uv pip list                        # Show installed
uv pip freeze > requirements.txt   # Save
uv pip install -r requirements.txt # Install from file
```

### 10. uv — Project Management (Best Way)

```bash
uv init my_project                 # Create project with pyproject.toml
cd my_project
uv add numpy                      # Add dependency (auto-creates venv + lockfile)
uv add pandas matplotlib          # Add multiple
uv remove numpy                   # Remove dependency
uv sync                           # Install all from lockfile
uv run python main.py             # Run script (no activate needed!)
uv run jupyter notebook           # Run any command inside venv
```

### 11. uv — Python Version Management

```bash
uv python list                    # List available Python versions
uv python install 3.12            # Install Python 3.12
uv venv --python 3.12             # Create venv with specific version
```

---

## pip vs uv — Comparison

| Task | pip + venv | uv |
|------|-----------|-----|
| Create venv | `python3 -m venv .venv` | `uv venv` |
| Install package | `pip install numpy` | `uv pip install numpy` |
| Add to project | `pip install` + `pip freeze` | `uv add numpy` |
| Run in venv | activate + `python main.py` | `uv run python main.py` |
| Lock dependencies | pip-tools (separate) | Built-in (`uv.lock`) |
| Install Python | pyenv (separate) | `uv python install` |
| Speed | Slow | **10-100x faster** 🚀 |

---

## Quick Reference

```bash
# --- Traditional ---
python3 -m venv .venv              # Create
source .venv/bin/activate           # Activate
pip install numpy                   # Install
pip freeze > requirements.txt       # Save

# --- Modern (uv) ---
uv venv                            # Create
uv pip install numpy                # Install (fast!)
uv init my_project                  # New project
uv add numpy pandas                 # Add deps
uv run python main.py              # Run (no activate!)
uv sync                            # Install from lockfile
```

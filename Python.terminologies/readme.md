Sure! Here's a clean and well-structured version of all the **Python and programming definitions** you asked for, ready to copy into your `glossary.md` file on GitHub:

---

# 📘 Python Terminologies – Glossary

A beginner-friendly dictionary of Python and core programming concepts with concise definitions.

---

### 1. **Compiled Language**

A compiled language requires the entire source code to be translated into machine code by a **compiler** before it can be executed by the computer.
✅ Example: C, C++

---

### 2. **Interpreted Language**

An interpreted language executes code **line by line** using an **interpreter**, without prior conversion to machine code.
✅ Example: Python, JavaScript

---

### 3. **Byte Code**

Byte code is an **intermediate representation** of your code, which is not human-readable but is **platform-independent**. It is generated after compilation and executed by a virtual machine.
✅ Python stores it in `.pyc` files.

---

### 4. **Compiler**

A compiler is a program that **translates source code** into **machine code** or **byte code** all at once.
✅ Output: Object files or Executables.

---

### 5. **Linker**

A linker takes one or more **object files** (compiled code) and **links** them with libraries to produce a single **executable** program.

---

### 6. **PVM (Python Virtual Machine)**

The Python Virtual Machine (PVM) is a part of the Python interpreter. It reads **bytecode** (`.pyc` files) and executes it.
✅ Acts as the runtime engine for Python programs.

---

### 7. **.pyc (Python Compiled Code)**

`.pyc` files are **compiled bytecode** files automatically created by Python when a module is imported.
✅ They help improve performance by avoiding recompilation.

---

### 8. **Object Code**

Object code is the **binary output** produced by a compiler before final linking. It’s not yet executable but is a key step in the compilation process.

---

### 9. **Interpreter**

An interpreter reads and **executes source code line by line**.
✅ Python uses an interpreter for executing bytecode.

---

### 10. **Executable**

An executable file is a program that can run directly on an operating system.
✅ Example: `.exe` files in Windows

---

### 11. **Statements**

A statement is a single instruction in a program that performs an action.
✅ Example:

```python
x = 5
print(x)
```

---

### 12. **Variable**

A variable is a **named storage location** used to hold data in memory.
✅ Example:

```python
name = "Siddharth"
```

---

### 13. **Identifier**

An identifier is the **name** used to identify variables, functions, classes, modules, etc.
✅ Rules: Must begin with a letter or underscore and not be a keyword.

---

### 14. **Keyword**

Keywords are **reserved words** in Python with predefined meanings.
❌ Cannot be used as variable names.
✅ Examples: `if`, `for`, `class`, `return`, `True`, `None`

---

### 15. **Comments**

Comments are notes written in code that are **ignored by the interpreter**.
Used for explaining code logic.
✅ Example:

```python
# This is a comment
```

---

### 16. **Symbol Table**

The symbol table is an internal **data structure** that tracks:

* **Name**: The identifier (e.g., variable or function)
* **Value**: The data it holds
* **Data Type**: Type of the data (e.g., int, str)
* **Address**: Memory location of the value

It helps in **memory management and scope resolution** during program execution.

---

### 17. **Memory Block / Memory Box**

A memory block (or memory box) refers to a **logical container** in RAM where variable data is stored.
✅ Think of it like a labeled box storing a value.

---

### 18. **Memory Address**

The memory address is the **unique location** in RAM where a variable or object is stored.
✅ In Python, you can check it using:

```python
x = 10
print(id(x))
```


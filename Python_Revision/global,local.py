### ✅ 1. **Global and Local Scope**

# * **Local Scope**: Variables declared inside a function. They only exist within that function.
# * **Global Scope**: Variables declared outside any function. They can be accessed anywhere in the file.

#### 🔹 Example:

# ```python
x = 10  # Global variable

def my_func():
    y = 5  # Local variable
    print("Inside function, x:", x)  # accessing global
    print("Inside function, y:", y)

my_func()

print("Outside function, x:", x)
# print("Outside function, y:", y)  # ❌ Error: y is not defined outside


### ✅ 2. **Use of `global` keyword**

# * Used to **modify a global variable** inside a function.

#### 🔹 Example:

# ```python
count = 0  # Global variable

def increment():
    global count  # tells Python to use the global variable
    count += 1

increment()
increment()
print("Count is:", count)  # Output: 2


# Without `global`, it would create a **new local variable**, and you'd get an error when trying to modify the global one.


### ✅ 3. **Variable Argument Function (`*args`)**

# * Used when you want to **pass a variable number of non-keyword arguments** to a function.
# * Inside the function, `args` is a **tuple**.

#### 🔹 Example:

# ```python
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Total:", total)

add_numbers(10, 20)
add_numbers(5, 10, 15, 20)

### ✅ 4. **`**kwargs` (Keyword Arguments)**

# * Used when you want to **pass variable number of keyword arguments**.
# * Inside the function, `kwargs` is a **dictionary**.

#### 🔹 Example:

# ```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Siddharth", age=27, location="Pune")

### ✅ Combine `*args` and `**kwargs`

# You can use both in the same function.

#### 🔹 Example:

# ```python
def mix_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

mix_args(1, 2, 3, name="Sid", role="PM")


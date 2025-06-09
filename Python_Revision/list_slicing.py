### 🔹 Syntax of Slicing


# * `start`: index to start from (inclusive)
# * `stop`: index to stop (exclusive)
# * `step`: how much to move forward (default is `1`)

### 📘 Example List

numbers = [10, 20, 30, 40, 50, 60, 70]
# Indexes:   0   1   2   3   4   5   6

### ✅ Basic Slicing Examples

print(numbers[1:5])     # Output: [20, 30, 40, 50]

# * Starts at index 1 → 20
# * Stops before index 5 → stops at 50
# * Step is 1 by default


### 🔸 Start and Stop

print(numbers[:4])      # Output: [10, 20, 30, 40]
print(numbers[3:])      # Output: [40, 50, 60, 70]

# * `[:4]`: From start (index 0) to index 4 (excluded)
# * `[3:]`: From index 3 to the end

### 🔸 Step

print(numbers[0:7:2])   # Output: [10, 30, 50, 70]

# * Start at 0
# * Go till index 6 (7 excluded)
# * Step by 2

### 🔸 Negative Step (Reversing a list)

print(numbers[::-1])    # Output: [70, 60, 50, 40, 30, 20, 10]

# * Reverses the list

print(numbers[5:1:-1])  # Output: [60, 50, 40, 30]

# * Start at index 5 (60)
# * Stop before index 1
# * Step back by 1


### ⚠️ Important Rules

# | Behavior      | Example  | Explanation                |
# | ------------- | -------- | -------------------------- |
# | Start omitted | `[:3]`   | Starts from beginning      |
# | Stop omitted  | `[3:]`   | Goes till end              |
# | Step omitted  | `[1:5]`  | Step defaults to 1         |
# | All omitted   | `[:]`    | Returns a copy of the list |
# | Negative step | `[::-1]` | Reverses the list          |

### 📌 Summary

# | Part  | Meaning                              |
# | ----- | ------------------------------------ |
# | Start | Index to begin slicing (inclusive)   |
# | Stop  | Index to stop slicing (exclusive)    |
# | Step  | Jump size (how many indices to skip) |
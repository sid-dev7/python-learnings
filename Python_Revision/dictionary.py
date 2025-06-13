# # Dictionary of student marks
# student_marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 76
# }

# # Access by key
# print("Bob's marks:", student_marks["Bob"])

# # Update value
# student_marks["Charlie"] = 80

# # Add new entry
# student_marks["David"] = 90

# print("All student marks:", student_marks)

# operations on dictionary
student = {
    "name": "Alice",
    "age": 22,
    "marks": 88
}
# 🔍 1. Access Elements
print(student["name"])   # Output: Alice
print(student.get("age"))  # Output: 22
print(student.get("grade", "Not Found"))  # Avoids error, returns default

# 📝 2. Add or Update Values

student["grade"] = "A"         # Add new key
student["marks"] = 90          # Update existing key

print(student.get("marks")) 
print(student.get("grade")) 
# ❌ 3. Remove Elements

student.pop("age")             # Removes 'age' key
del student["grade"]           # Removes 'grade' key
student.clear()                # Clears all entries

# 🔄 4. Loop Through Dictionary

# Sample dictionary
student = {"name": "Alice", "marks": 90, "grade": "A"}

# Loop keys
for key in student:
    print(key)

# Loop values
for value in student.values():
    print(value)

# Loop key-value pairs
for key, value in student.items():
    print(key, ":", value)

# 🧪 5. Check Existence of Key

print("marks" in student)    # True
print("age" in student)      # False

# 📏 6. Length of Dictionary
print(len(student))  # Number of key-value pairs

# 🧱 7. Copy a Dictionary
student_copy = student.copy()

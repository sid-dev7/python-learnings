
# ```python
my_list = [10, 20, 30, 40, 30]

## ✅ 1. `len()` – Get Length

my_list = [10, 20, 30, 40, 30]
print("Length of list:", len(my_list))  # Output: 5

## ✅ 2. `append()` – Add item at the end


my_list.append(50)
print("After append:", my_list)  # Output: [10, 20, 30, 40, 30, 50]


## ✅ 3. `insert()` – Insert at specific position

my_list.insert(2, 25)
print("After insert at index 2:", my_list)  # Output: [10, 20, 25, 30, 40, 30, 50]

## ✅ 4. `pop()` – Remove and return item at given index (default: last)

last_item = my_list.pop()
print("After pop:", my_list)        # Output: [10, 20, 25, 30, 40, 30]
print("Popped item:", last_item)    # Output: 50

item_at_index_1 = my_list.pop(1)
print("After pop at index 1:", my_list)  # Output: [10, 25, 30, 40, 30]


## ✅ 5. `remove()` – Remove first occurrence of a value

my_list.remove(30)
print("After remove 30:", my_list)  # Output: [10, 25, 40, 30]

# > ⚠️ If the item doesn't exist, you'll get a `ValueError`.

## ✅ 6. `count()` – Count how many times a value appears

count_30 = my_list.count(30)
print("Count of 30:", count_30)  # Output: 1

## ✅ 7. `index()` – Find index of first occurrence of a value

index_40 = my_list.index(40)
print("Index of 40:", index_40)  # Output: 2

## ✅ 8. `clear()` – Remove all items from the list


my_list.clear()
print("After clear:", my_list)  # Output: []

## ✅ 9. `extend()` – Add all items from another list

my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print("After extend:", my_list)  # Output: [1, 2, 3, 4, 5, 6]

## 📌 Final Recap Table

# | Operation  | Description                          | Example                  |
# | ---------- | ------------------------------------ | ------------------------ |
# | `len()`    | Length of list                       | `len(my_list)`           |
# | `append()` | Add to end                           | `my_list.append(10)`     |
# | `insert()` | Add at index                         | `my_list.insert(2, 99)`  |
# | `pop()`    | Remove item (last or at index)       | `my_list.pop()`          |
# | `remove()` | Remove by value                      | `my_list.remove(30)`     |
# | `count()`  | Count how many times a value appears | `my_list.count(30)`      |
# | `index()`  | Get index of a value                 | `my_list.index(40)`      |
# | `clear()`  | Remove all elements                  | `my_list.clear()`        |
# | `extend()` | Add multiple elements                | `my_list.extend([1, 2])` |



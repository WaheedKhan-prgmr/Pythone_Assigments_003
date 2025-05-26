# Sets


numbers = {1, 2, 3, 2, 1, 1, 2, 3, 2, 1}
print("Set (no duplicates):", numbers)

numbers.add(4)
print("After adding 4:", numbers)

numbers.remove(2)
print("After removing 2:", numbers)

# Frozensets (Immutable Sets)


immutable_set = frozenset([1, 2, 3, 3])
print("Frozenset:", immutable_set)

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)

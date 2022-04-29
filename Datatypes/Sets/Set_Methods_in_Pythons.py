set_1 = {1, "Hello", 'A', False}

# len()
print("Number of Elements in set_1 =", len(set_1))

# removal using "remove" and "pop"
set_1.remove('A')
print("After removal :", set_1)
print("Number of Elements :", len(set_1))

set_1.pop()  # removes an element "randomly"
print("After removal :", set_1)
print("Number of Elements :", len(set_1))

# Clear
set_1.clear()
print("After clearing :", set_1)
print("Number of Elements :", len(set_1))

# Union of Sets
set1 = {1, "Hello", 'A'}
set2 = {2, "World", 'B'}
print("Union :", set1.union(set2))

# Intersection of Sets
set3 = {1, 2, 3, 4, 5}
set4 = {3, 4, 5, 6, 7}
print("Union :", set3.intersection(set4))

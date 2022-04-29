# Set ignores repetitions
# Sets are unordered unlike lists

set_a = {1, 'A', "Hello", 'A'}
print("Set_a :", set_a)
set_b = {1, True, 0, False}
print("Set_b :", set_b)

# Creating an Empty Set
set_empty1 = {}  # Creates an empty dictionary and not an empty set
print(type(set_empty1))
set_empty2 = set()  # Creates an empty set
print(type(set_empty2))

# Adding elements to a set
set_empty2.add("World")
print(set_empty2)

# set_empty2.add([1,2,3]) throws an error as "You can't add a list/dictionary to a set" but "You can add a tuple to a set"
# set_empty2.add({"Hello" : "World"})
# you can only add "hashable"(Can not be changed / has constant hash value during its lifetime) elements in a set
set_empty2.add((1, 2, 3))
print(set_empty2)

# "numbers" and "strings" are not counted as same
# 20 and 20.0 are counted as same as the values are equal (just like 1/0 or True/False)
set_ab = {1, '1', 1.0}
print(set_ab)

t = (True, 1, "Hello", False, "World", 1, 2, 1)

# counting number of occurences
print(t.count(1))  # True/False are also counted as '1'/'0'
print(t.count(True))  # True/False counts (Trues/1s) / (Falses/0s)
print(t.count(0))
print(t.count(False))

# index search (First Occurence)
print(t.index("World"))
print(t.index(True))
print(t.index(1))
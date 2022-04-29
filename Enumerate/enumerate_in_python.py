list1 = [3, 'A', True, "Hello World!!!"]

# to print the list contents with the index number ...

# index = 0
# for items in list1:
#     print(index, items)
#     index += 1

# we can instead use enumerate
# enumerates adds a counter to the iterables and returns it just like in the above code
for index, items in enumerate(list1):
    print(index, items)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# METHOD 1
# b = []
# for items in a:
#     if(items%2==0):
#         b.append(items)

# print(b)

# METHOD 2 (Shortcut)
b = [items for items in a if items % 2 == 0]
print(b)

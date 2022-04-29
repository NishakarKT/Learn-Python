def square(num):
    return num*num


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# METHOD 1
list2 = []
for i in list1:
    list2.append(square(i))
print(list2)

# METHOD 2
list3 = list(map(square, list1))  # map(func, input list) typecasted to list
print(list3)

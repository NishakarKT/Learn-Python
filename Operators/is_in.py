num1 = 50
num2 = None
set_1 = {1,2,3,4,5}
list_1 = [1,2,3,4,5]
tuple_1 = (1,2,3,4,5)

# is (similar to "==")
if(num1 is 50):
    print("num1 = 50")
else:
    print("num1 != 50")

print("num1 is 50 =", num1 is 50)
print("num2 is nONE =", num2 is None)

# in (can be used to check if an element is present in a list/set/tuple)
print("3 in set_1 =", 3 in set_1)
print("6 in set_1 =", 6 in set_1)
print("3 in list_1 =", 3 in list_1)
print("6 in list_1 =", 6 in list_1)
print("3 in tuple_1 =", 3 in tuple_1)
print("6 in tuple_1 =", 6 in tuple_1)
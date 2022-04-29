str1 = "Hello World!!!"

# STRING SLICING
print(str1[1:3])  # includes index = 0,1 and 2 (NOT 3).
print(str1[:3])  # automatically adds '0' to left
print(str1[3:])  # automatically adds 'string length value = 14' to right

# Skipping Values
print(str1[0:14:1])  # same as "print(str1[0:14])"
print(str1[0:14:2]) # skips 2 at a time --> index 0,2,4,6,8,10,12 (<14 (14 not included))
print(str1[0::3])   # automatically fills the (string length value in the middle spot) --> 0,3,6,9,12
print(str1[::4])    #  indices printed --> 0,4,8,12
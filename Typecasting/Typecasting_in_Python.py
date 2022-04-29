a = '12340'

# here 'a' is a String
# so print(a + 5) is not valid.
# So we typecast string 'a' into int 'a'

print(int(a) + 5)

print("'a' is of", type(a), "even after using its typecasted form in a statement earlier.")

a = int(a)  # coverting string 'a' to int 'a'
print("'a' is of", type(a), "after typecasting it to int")

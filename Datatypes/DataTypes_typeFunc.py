# type() displaays the data type of the input.

# Python Datatypes

# (1) number
print(type(123))  # int
print(type(12.3))  # float
print(type(1j))  # complex

# (2) string -------------------------------------
print(type('Hello World'))  # string
a = ('apple', 'banana', 'orange')
print(type('a'))  # string

# declaring a string
# 1
a = '\"Hello World!!!\"'
print(a)
# 2
a = "\"Hello World!!!\""
print(a)
# 3
a = '''"Hello World!!!"'''  # we dont have to worry about (\") if we use triple quotes to make string literals.
# but you can't have escape sequence chracters if you use triple quotes.
print(a)

# (3) sequence ------------------------------------
a = ["apple", "banana", "orange"]
print(type(a))  # list
a = ("apple", "banana", "orange")
print(type(a))  # tuple
a = range(6)
print(type(a))

# (4) sets ---------------------------------------
a = {"john", "age", 36}
# a = {1,2,3,'a','b', c} #error
a = {1, 2, 3, 'a', 'b', 'c'}
print(type(a))  # set
a = frozenset({1, 2, 3, 'a', 'b', 'c'})
print(type(a))  # frozen set

# (4) boolean ------------------------------------
a = True
print(type(a))  # bool
print(a)
print(int(a))

# (5) binary -------------------------------------
a = b"hello"
print(type(a))
a = bytearray(5)
print(type(a))
a = memoryview(bytes(5))
print(type(a))

# (6) mapping ------------------------------------
a = {"hello": "world", "phone": "number"}
print(type(a))  # dict

# (7) none ---------------------------------------
a = None  # similar to null
print(a)

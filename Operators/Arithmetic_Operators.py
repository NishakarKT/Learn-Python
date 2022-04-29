x = 12
y = 8

sum = (x+y)
sub = (x-y)
prod = (x*y)
div = (x/y)

print(type(sum))
print(type(sub))
print(type(prod))
print(type(div))
print(type(int(div)))  # typecasting
print("\n")

############################################### Positioning Method 1 (Better Method) ################################################
print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(x, "*", y, "=", x*y)
print(x, "/", y, "=", x+y)
print(x, "//", y, "=", x//y)
print(x, "**", y, "=", x**y)

x += 5
y -= 5
print("x = ", x, "\ny = ", y)
x *= 2
y /= 2
print("x = ", x, "\ny = ", y)
x **= 2
y //= 2
print("x = ", x, "\ny = ", y)
print("\n")

############################################### Positioning using format (Method 2) ################################################
#position = {index}
print("{0} + {1} = {2}\n".format(x, y, sum))
print('{0} - {1} = {2}\n'.format(x, y, sub))
print("{0} * {1} = {2}\n".format(x, y, prod))
print('{0} / {1} = {2}\n'.format(x, y, div))


print('{0} / {1} = {2}\n'.format(x, y, int(div)))  # typecasting
# //' is just like typecasting to int
print('{0} / {1} = {2}\n'.format(x, y, x//y))
print("{0} % {1} = {2}".format(x, y, x % y))

# ** is like power function m**n gives pow(m,n) operator
print("{0} ** {1} = {2}\n".format(2, 3.5, 2**3.5))

###############################################  ################################################

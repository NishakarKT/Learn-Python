x = 12
y = 8

############################################### Positioning Method 1 (Better Method) ################################################
print(x, "+", y, "=", x+y)
print(x, "-", y, "=", x-y)
print(x, "*", y, "=", x*y)
print(x, "/", y, "=", x+y)
print("")

############################################### Positioning using format (Method 2) ################################################
#position = {index}
print("{0} + {1} = {2}".format(x, y, x+y))
print("{} + {} = {}".format(x, y, x+y)) # by default it is ordered (0, 1, 2, ....)
print("{0} - {1} = {2}".format(x, y, x-y))
print("{0} * {1} = {2}".format(x, y, x*y))
print("{0} / {1} = {2}".format(x, y, x/y))
print("")
############################################### Positioning using f strings (Method 3) ################################################

print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")

###############################################  ################################################

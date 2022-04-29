def func1(a):
    return a+5
x = 555
print(func1(x))

# another way to code the above using Lambda Functions...

func2 = lambda a : a+5 # labda arguments:expressions
# generally used to pass functions in functions
print(func2(x))
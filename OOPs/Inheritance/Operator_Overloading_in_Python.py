class number:
    def __init__(self, num1):
        self.num = num1

    def __add__(self, num2):  # to overload "+" we have to use "__add__" (It's in the Python Docs)
        print("Let's add")
        return self.num + num2.num

    def __mul__(self, num2):  # to overload "*" we have to use "__mul__" (It's in the Python Docs)
        print("Let's multiply")
        return self.num * num2.num

    def __str__(self):
        return f"Decimal Number : {self.num}"

    # my methods
    def __len__(self):
        return 1


num1 = number(4)
num2 = number(6)

num1 + num2  # executes "__add__" function... "__add__" is recognised by "+" operator
print(num1 + num2)
num1 * num2
print(num1 * num2)

# this shows a weird output but if we have to show the decimal number it holds, we define "def __str__"...
print(num1)

# defining my method
print(len(num1))
print(len(num2))

def add(num1, num2):
    return num1 + num2

print(__name__) # returns module's name

# we code like the following to avoid execution of the following code as we only need the functions of this imported file
if __name__ == "main":  # value of __name__ for the original file is "main"
    print(add(2, 3))

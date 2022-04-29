def greet(name):
    print(f"Good Morning {name}")

print(__name__) # returns module's name

# we code like the following to avoid execution of the following code as we only need the functions of this imported file
if __name__ == "__main__" : # value of __name__ for the original file is "main"
    user = input("Enter your name : ")
    greet(user)
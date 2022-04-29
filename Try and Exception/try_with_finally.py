try:
    i = int(input("Enter a number : "))
    c = 1/i
except Exception as e:
    print(e)
    exit()

# IN CASE OF AN EXCEPTION
finally:  # this will execute even if you have already coded the exit()
    print("Finally's code will execute no matter what !!!")

# this won't execute as the program exits by using exit ()
print("Hello World!!")

# in the following code if the user inputs a special character (ex: '#','%' etc.) in place of an integer...
# it will throw an error and the program crashes...
# so we use try, which will try the code, if it works, the code is executed, else not (program doesn't crash)
try:
    user = int(input("Enter a Number : "))
    print(user + 10)
except Exception as e:  # to display the error
    print(e)

# only shows the first error satisfied and breaks out of the ladder ...
try:
    a = int(input("Enter a Number : "))
    print("Hello" + 123)  # Type Error
    c = 1/a
    print(c)
except ValueError as e:
    print(e)  # here 'e' is the value error and we are printing it
except TypeError as e:
    print(e)  # here 'e' is the type error and we are printing it
except ZeroDivisionError as e:
    print(e)  # here 'e' is the zero division error (n/0) and we are printing it

print("\nCode is successfully executed...printing the error if any...")

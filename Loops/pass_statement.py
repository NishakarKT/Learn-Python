num = 12

if(num > 10):
    pass  # pass statement is similiar to NULL statement. It instructs to do "NOTHING"
# if instead of pass statement, you leave the code block blank, it will throw an error.
elif(num < 13):
    print("num < 13")
else:
    print("num == 12")

# As only one statement is executed in an if-elif-else ladder, the first statement is executed and it was a "pass" statement, so nothing happened.

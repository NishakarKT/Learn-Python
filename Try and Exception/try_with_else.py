try:
    i = int(input("Enter a Number : "))
    c = 1/i
except Exception as e:
    print(e)
else: # else's code is executed if the try's code executes successfully
    print("Code executed successsfully ...")
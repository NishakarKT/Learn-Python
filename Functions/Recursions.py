def fibonacci(num):
    if(num == 1):
        return 0
    if(num == 2):
        return 1
    return fibonacci(num-1) + fibonacci(num-2)


num = int(input("Enter number of Fibonacci members you want to display : "))

for i in range(1,num+1):
    print(fibonacci(i)," ", end="")

def factorial(num):
    p = 1
    for i in range(2, num+1):
        p *= i
    return p

for i in range(11):
    print(f"{i} ! = {factorial(i)}")

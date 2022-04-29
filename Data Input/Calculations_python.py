num1 = input("Enter num 1 : ")
num2 = input("Enter num 2 : ")

# print(num1,"+",num2,"=", num1+num2) throws an error as we get user input as strings and we can't add 2 strings arithmetically.

print(num1,"+",num2,"=", int(num1) + int(num2))
print(num1,"-",num2,"=", int(num1) - int(num2))
print(num1,"*",num2,"=", int(num1) * int(num2))
print(num1,"**",num2,"=", int(num1) ** int(num2))
print(num1,"/",num2,"=", int(num1) / int(num2))
print(num1,"//",num2,"=", int(num1) // int(num2))
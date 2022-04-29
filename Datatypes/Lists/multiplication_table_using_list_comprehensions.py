num = int(input("Enter a Number : "))
mem = int(input("Number of members of the Table : "))

table = [num*i for i in range(1, mem+1)]
print(table)
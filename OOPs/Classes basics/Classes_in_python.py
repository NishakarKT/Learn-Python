# class student:
#     def print_data(self):
#         print(f"Name : {self.name}\tRoll = {self.roll}")


# student1 = student()
# student1.name = "Aman"
# student1.roll = 1
# student1.print_data()

###################################################

class employee:
    company = "Google"  # class attribute
    salary = 100  # class attribute


raj = employee()
simran = employee()
print(raj.company, "\t", simran.company)
# "company" is a Class Attribute and by this way changes will be refelected in all other objects.
employee.company = "Youtube"
print(raj.company, "\t", simran.company)

# but if we want to make attributes personal to the object, they have higher priority compared to a class atribute with the same name.
# raj.salary = 400 # instance attribute
# simran.salary = 500 # instance attribute
print(raj.salary, "\t", simran.salary)

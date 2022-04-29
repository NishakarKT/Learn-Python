class student:
    name_student = "Rohan"

    def print_student(self):
        print(f"Student name : {self.name_student}")


class employee:
    name_employee = "Mathur"

    def print_employee(self):
        print(f"Employee name : {self.name_employee}")


# Inheriting attributes of both the classes
class data(student, employee):
    def __init__(self):
        print("Hello !!!")
    # def print_student(self): # Higher priority for a object of class "data"
    #     print("The inherited class's method \"print_student()\" runs...")


obj = data()
obj.print_employee()
obj.print_student()

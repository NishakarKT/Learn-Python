# >>> Here we change the "Instance Attribute" and not the "Class Attribute"

# class employee:
#     company = 'Camel'
#     salary = 100
#     location = 'Delhi'

#     def change_salary_to(self, sal):
#         self.salary = sal

# E1 = employee()
# print(E1.salary)
# E1.change_salary_to(200)
# print(E1.salary)
# print(employee.salary)

# >>> Changing class attribute >> Method 1
# class employee:
#     company = 'Camel'
#     salary = 100
#     location = 'Delhi'

#     def change_salary_to(self, sal):
#         self.__class__.salary = sal # .__class__. changes both the Class and  Instance Attributes


# E1 = employee()
# print(E1.salary)
# E1.change_salary_to(200)
# print(E1.salary)
# print(employee.salary)

# >>> Changing class attribute >> Method 2
class employee:
    company = 'Camel'
    salary = 100
    location = 'Delhi'

    @classmethod  # code a decorator "classmethod"
    def change_salary_to(cls, sal):
        cls.salary = sal


E1 = employee()
print(E1.salary)
E1.change_salary_to(200)
print(E1.salary)
print(employee.salary)

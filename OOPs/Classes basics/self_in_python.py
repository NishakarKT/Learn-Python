class employee:
    def print_data(self):
        print(f"Salary = {self.salary}")


obj1 = employee()
obj1.salary = 25000

obj1.print_data()
# self converts the above line as following
employee.print_data(obj1)

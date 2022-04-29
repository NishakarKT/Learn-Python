class Employee:
    company = 'Bharat Gas'
    salary = 45000
    salary_bonus = 5000
    # total_salary = 50000 # if I hard code the "total salary", if tomorrow I have to change the salary bonus of the employee, I have to change the "total_salary" as well.

    # GETTER
    @property  # behaves as a property
    def total_salary(self):
        return self.salary + self.salary_bonus
    
    #SETTER
    @total_salary.setter
    def total_salary(self, sal):
        self.salary_bonus = sal - self.salary # if I change my total_salary, salary_bonus is changed to adjust to it....


E1 = Employee()

print("Initial Salary :", E1.salary)
print("Initial Salary Bonus :", E1.salary_bonus)
print("Initial Total Salary :", E1.total_salary)
print("")

E1.salary_bonus = 10000

print("Final Salary 1 :", E1.salary)
print("Final Salary Bonus 1 :", E1.salary_bonus)
print("Final Total Salary 1 :", E1.total_salary)
print("")

E1.total_salary = 60000
print("Final Salary 2 :", E1.salary)
print("Final Salary Bonus 2 :", E1.salary_bonus)
print("Final Total Salary 2 :", E1.total_salary)
print("")
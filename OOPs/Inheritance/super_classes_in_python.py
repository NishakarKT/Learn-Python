class student:
    Group = "students"

    def greet(self):
        print("Good Morning...")


class tech_enthusiast(student):
    Group = "tech enthusiasts"

    def greet(self):
        super().greet()  # this again traces back to the next latest parent upwards and comeback after execution
        print("Good Afternoon...")


class programmer(tech_enthusiast):
    Group = "programmers"

    def greet(self):
        super().greet()  # this executes the greet function of latest parent class's "greet()"
        # print("Good Night...")


obj1 = student()
print(obj1.greet())

obj2 = tech_enthusiast()
print(obj2.greet())

obj3 = programmer()
print(obj3.greet())

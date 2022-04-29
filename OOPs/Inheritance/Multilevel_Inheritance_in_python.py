class student:
    Group = "students"

    def greet(self):
        print("Good Morning...")


class tech_enthusiast(student):
    Group = "tech enthusiasts"

    def greet(self):
        print("Good Afternoon...")


class programmer(tech_enthusiast):
    Group = "programmers"
    # def greet(self):
    #     print("Good Night...")


obj1 = student()
print(obj1.greet())

obj2 = tech_enthusiast()
print(obj2.greet())

obj3 = programmer()
print(obj3.greet())

# uses the latest parent's function in cases of same name ambiguities.

class student:
    ID = 123

class teacher:
    ID = 987

class data(student, teacher):
    def __init__(self):
        print("Data :")
    
obj = data()
# out of 2 IDs , ID of student class is printed as while inheriting we write "student" first
print(obj.ID)
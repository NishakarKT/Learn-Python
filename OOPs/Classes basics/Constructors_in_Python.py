class hello_world:
    def __init__(self):  # takes atleast "self" argument
        print("Hello World!!!")


obj = hello_world()  # constructors execute right at the time of assignment

#########################################################################################
class complex:
    real = 0
    imaginary = 0
    def __init__(self, re, im):
        self.real = re
        self.imaginary = im
    
    def print_complex(self):
        print(f"{self.real} + i({self.imaginary})")

Z1 = complex(1,2)
Z1.print_complex()

#########################################################################################
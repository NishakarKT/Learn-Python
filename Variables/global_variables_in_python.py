num = 10  # global variable


def increment1():  # as no num local variable "num" is present, global variable is accessed.
    return num+1  # num can be accessed by any function.


def increment2():
    num = 20  # local variable (higher priority)
    return num+1  # num can be accessed by any function.


def increment3():
    global num  # now global variable is accessed.
    num = 20  # global variable "num" is reassigned.
    return num+1


print("global \"num\" incremented value =", increment1())
print("local \"num\" incremented value =", increment2())
print("global \"num\" incremented value =", increment3())
print("global variable \"num\" final value =", num)


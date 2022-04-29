class sample:
    def age_print(self):
        print(f"Age = {self.age}")
    # if we don't require an object in the function, we may define a function the following way,

    @staticmethod  # declaring a static method/function
    def greet():
        print("Good Morning...")


obj = sample()
obj.age = 25

sample.age_print(obj)  # we pass the object "obj"
sample.greet()  # we dont have to pass any parameter

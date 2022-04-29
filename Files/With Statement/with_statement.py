#using with, you dont have to expilicitly code about closing the file, it automatically closes the file.
with open("sample.txt", "w") as f:
    f.write("Hello Jupiter !!!")
with open("sample.txt", "r") as f:
    a = f.read()

print(a)
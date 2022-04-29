# f = open("sample.txt", "r")  # opening file in reading mode (Default)
# f = open("sample.txt", "rt")  # t = text mode(default) // rb --> binary mode
f = open("sample.txt")

# you can read a file only once after opening
print("File's Data : " + f.read())
# print("File's Data : " + f.read(5))  # Reads 5 characters

# closing a file --> Always close a file after use
f.close()

import File1
import File2

# for __name__ in imported files, "filename" is returned
print(__name__) # displays "main"

File1.greet("Nishakar Kumar") # this also runs the contents of File 1 which we don't want. We only need the greet() function.
# print(File2.add(2,3))
f = open("writing.txt", "w")  # in writing mode
# Automatically creates a .txt file if not present in the present directory
# it also "completely" overwrites any initial content in the opened file

# once opened it no longer overwrites the over-written content in the same opened mode, it instead adds on...
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")
f.write("Hello Mars!!!\n")

f.close()

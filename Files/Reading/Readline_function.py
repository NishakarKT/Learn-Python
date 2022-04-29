f = open("sample.txt")

print(f.readline())  # Reads the first line from top when used once
print(f.readline())  # Reads the second line from top when used twice
# and so on...

f.close()

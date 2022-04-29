# Pattern.
n = 5

# end statement --> "what should the line end with".
# Example --> end = " ", --> line ends with a space.
# by default --> end = "\n".
for i in range(5):
    print("  " * (n-i-1), end="")
    print("* " * (2*i+1), end="")
    print("  " * (n-i-1))

# renaming similar to "copy new file and delete original file"

import os

# reading
with open("sample.txt") as f:
    content = f.read()

# deleting
os.remove("sample.txt")

# copying
with open("sample.txt", "w") as f:
    f.write(content)

# Used for Mapping
# They are unordered unlike lists

myDict = {"happy": "feeling or showing pleasure or contentment",
          "sad": "feeling or showing sorrow",
          "marks": [24, 21, 23, 22, 25],
          "myDict2": {"Nishakar": "Kumar"}}

# Accessing elements in Dictionary
print("Happy :", myDict["happy"])
print("Sad :", myDict["sad"])
print("Marks :", myDict["marks"])
print("myDict2 :", myDict["myDict2"])  # Another Dictionary in a Dictionary
print("myDict2 :", myDict["myDict2"]["Nishakar"]) # Accessing elements of this Second Dictionary

# They are Mutable(Changable)
myDict["marks"] = [1,2,3,4,5]
myDict["marks"][2] = 24
print(myDict["marks"])

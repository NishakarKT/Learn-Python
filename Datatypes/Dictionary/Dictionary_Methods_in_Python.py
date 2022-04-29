myDict = {"happy": "feeling or showing pleasure or contentment",
          "sad": "feeling or showing sorrow",
          "marks": [24, 21, 23, 22, 25],
          "myDict2": {"Nishakar": "Kumar"},
          1: 10}
# Listing Dictionary Items
print(myDict.items())
print("")  # also adds newline

# Listing Keys
print(myDict.keys())
print("myDict.keys()", type(myDict.keys()))  # Datatype = "dict_keys"
print("Typecasted myDict.keys() :", type(list(myDict.keys())))
print("")  # also adds newline

# Listing Values
print(myDict.values())
print("myDict.values()", type(myDict.values()))  # Datatype = "dict_values"
print("Typecasted myDict.values() :", type(list(myDict.values())))
print("")  # also adds newline

# Updating Dictionary
update_dict = {"hello": "world",
               "python": "Coding Language"}

myDict.update(update_dict)  # Updating
myDict.update({"happy": "BirthDay"})  # Updating an existing entry

print(myDict.keys())
print(myDict.values())
print("")  # also adds newline

# Dict.get()

# both return same value
print(myDict.get("happy"))
print(myDict["happy"])

#but if a key is not present... (get doesn't throw an error and returns "None")
print(myDict.get("harry"))
# print(myDict["harry"]) ---> Throws error

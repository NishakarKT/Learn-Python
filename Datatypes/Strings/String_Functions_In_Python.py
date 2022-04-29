str1 = "hello World!!!"

##################################################################################################################
# String Length ---> len(str1) or len("Hello World!!!")
print("String Length =", len(str1))
print("String Length =", len("Hello World!!!"))

##################################################################################################################
# str1.endswith("str2") --> returns a bool whether a string 'str1' ends with a string 'str2'.
print("str1 ends with 'rld' =", str1.endswith("rld"))
print("str1 ends with '!!!' =", str1.endswith("!!!"))

##################################################################################################################
# str1.startswith("str2") --> returns a bool whether a string 'str1' starts with a string 'str2'.
print("str1 starts with 'Hel' =", str1.startswith("Hel"))
print("str1 starts with 'hel' =", str1.startswith("hel"))

##################################################################################################################
# Upper-casing
print("Upper Cased :", str1.upper())

# Upper-casing first letter
print("Capitalized string :", str1.capitalize())

##################################################################################################################
# Lower-casing
print("Lower Cased :", str1.lower())

##################################################################################################################
# Replacing --> string.replace("str1", "str2")
print("Replaced String :", str1.replace("World", "Earth"))
# Replacing string length doesn't matter
print("Replaced String :", str1.replace("orl", "oo"))

##################################################################################################################
# Counting specific character or a string
print("Number of o's =", str1.count("o"))
print("Number of !'s =", str1.count("!"))
print("Number of 'orl's =", str1.count("orl"))

##################################################################################################################
# Finding a character/sub-string in a string ((returns '-1' if not present))
print("'ello' is at index :", str1.find("ello"))
print("'llo' is at index :", str1.find("llo"))
print("'l' is at index :", str1.find("l"))  # Only records the first appearance

##################################################################################################################

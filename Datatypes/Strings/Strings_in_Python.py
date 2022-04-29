# a = 'it's me' throws an error as the interpreter is confused where the string ends with 3 single quotes

########################################################################################################################
# so we fix this as,
a = "It's me"
# similarly (1)
b = 'I am "Nishakar Kumar"'
# similarly (2)
c = '''It's "Nishkaar Kumar"'''

print(a)
print(b)
print(c)
########################################################################################################################

#IMPORTANT
# a[3] = 's' ---> Throws an error. You can't do this in a String.

###################################### String Indices ##################################################################

print("------")
print(a[-7])
print(a[-6])
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1]) # -1 returns the last index ---> Negtative indices are used in cases when you have no idea about the string's length.
print("------")
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print("------")

########################################################################################################################


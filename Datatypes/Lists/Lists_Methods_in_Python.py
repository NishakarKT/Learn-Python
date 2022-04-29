################################################# APPEND ####################################################
# "append" adds at the end of the list.
sample_list = [1, 2, 'hello']
sample_list.append('world')  # you can add only 1 item with append.
print("Appended List :", sample_list)

################################################# LIST SORTING ##################################################
list1 = [3, 1, 7, 2, 5, 4, 9, 6, 10, 8]
list1.sort()  # it doesn't RETURN a sorted list, it changes actual list.
print("Sorted list :", list1)

################################################# LIST REVERSING ##################################################
list1.reverse()
print("Reversed list :", list1)

################################################# LIST INSERTION ##################################################
list1.insert(3, 8)  # inserts '8' at index '3'.
print("Inserted list :", list1)

################################################# LIST POPPING ####################################################
list1.pop(3)  # removes element at index '3'.
print("Popped list :", list1)

################################################# LIST REMOVAL ####################################################
list1.remove(8)  # removes '8'.
print("Removed list :", list1)

################################################# LIST CLEAR ######################################################
list1.clear()  #inserts '8' at index '3'
print("Cleared list :",list1)

################################################# SUM #############################################################
a = [1,2,3,4,5]

print("Sum :", sum(a))
################################################# END #############################################################


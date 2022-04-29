def greater_than_5(num):
    return num > 5

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Initial List :", list1)
filtered_list1 = list(filter(greater_than_5, list1)) # filters the list for all the numbers greater than 5
print("Filtered List :", filtered_list1)

# using lambda functions
lambda_function_greater_than_5 = lambda num : num > 5
filtered_list2 = list(filter(lambda_function_greater_than_5, list1)) # filters the list for all the numbers greater than 5
print("Filtered List :", filtered_list2)

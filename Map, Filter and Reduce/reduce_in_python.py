from functools import reduce

sum = lambda a, b :a + b

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# summation of all the elements of the list
# "reduce" sums up sequentially
val = reduce(sum, list1)
print(val)

##############################################################
# MAX using reduce

def max(a,b):
    if(a>b):
        return a # if a>b, the return statement , returns 'a' and the function execution is terminated.
    return b

list2 = [23,11,28,32,11,10,18,47,36,92,31,67,35]
MAX = reduce(max, list2)
print("Max :", MAX)

for i in range(1,11):
    print(i)
else: # gives us an idea where a loop was executed completely or it was "break" somewhere
    print("The loop was executed completely.")

print("----------------")

for i in range(1,11):
    print(i)
    if(i == 6):
        break
else: # gives us an idea where a loop was executed completely or it was "break" somewhere
    print("The loop was executed completely.")
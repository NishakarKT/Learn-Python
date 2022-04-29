def increment(num):
    try:
        return int(num)+1
    except :
        raise ValueError("The argument passed must be a \"decimal\"...")

print(increment('3s'))
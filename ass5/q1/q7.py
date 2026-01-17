#Handle IndexError When Accessing a List
try:
    numbers = [10, 20, 30]
    print(numbers[5])

except IndexError:
    print("Error: Index out of range.")

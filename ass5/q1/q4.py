#Demonstrate Multiple Exception Blocks
try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)

except ValueError:
    print("Error: Invalid input.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

#Handle Invalid Integer Input
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)

except ValueError:
    print("Error: Please enter a valid integer.")

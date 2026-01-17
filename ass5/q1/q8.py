#Handle All Possible Errors (Two Numbers)
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)

except Exception as e:
    print("Error occurred:", e)

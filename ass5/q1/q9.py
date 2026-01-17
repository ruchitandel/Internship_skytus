#Log Errors to a File Instead of Printing
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)

except Exception as e:
    file = open("error_log.txt", "a")
    file.write(str(e) + "\n")
    file.close()
    print("Error saved to error_log.txt")

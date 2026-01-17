# 1. Voting Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print("--------------------------------")

# 2. Grade Calculator
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")
print("--------------------------------")

# 3. Traffic Light Simulation
signal = input("Enter traffic light color (red/yellow/green): ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")
print("--------------------------------")

# 4. ATM Withdrawal Check
balance = 5000
withdraw = int(input("Enter withdrawal amount: "))
if withdraw <= balance:
    print("Transaction successful.")
else:
    print("Insufficient balance.")
print("--------------------------------")

# 5. Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
print("--------------------------------")

# 6. Number in Range Check (10 to 50)
num = int(input("Enter a number: "))
if num >= 10 and num <= 50:
    print("Number is within the range.")
else:
    print("Number is outside the range.")
print("--------------------------------")

# 7. Username & Password Verification
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")
print("--------------------------------")

# 8. Electricity Bill Calculator
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = units * 3
else:
    bill = units * 5
print("Electricity Bill = ₹", bill)
print("--------------------------------")

# 9. Simple Calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operation")
print("--------------------------------")

# 10. Triangle Type Checker
a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

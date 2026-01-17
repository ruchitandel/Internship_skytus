# 1. Print numbers 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# 2. Multiplication table
n = int(input("Enter number for table: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# 3. Factorial
num = int(input("Enter number for factorial: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print("Factorial:", fact)

# 4. Fibonacci
terms = int(input("Enter number of terms for fibonacci: "))
a, b = 0, 1
for i in range(terms):
    print(a, end=" ")
    a, b = b, a+b
print("\n")

# 5. Prime check
num = int(input("Enter number to check prime: "))
flag = True
if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
print("Prime" if flag else "Not Prime")

# 6. Reverse number
num = int(input("Enter number to reverse: "))
rev = 0
temp = num
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10
print("Reversed:", rev)

# 7. Count digits
num = int(input("Enter number to count digits: "))
print("Digits:", len(str(num)))

# 8. Sum of even numbers (1–100)
total = 0
for i in range(2, 101, 2):
    total += i
print("Sum of even numbers:", total)

# 9. Pyramid pattern
rows = int(input("Enter rows: "))
for i in range(1, rows+1):
    print("* " * i)

# 10. Divisors
num = int(input("Enter number to find divisors: "))
print("Divisors:")
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")

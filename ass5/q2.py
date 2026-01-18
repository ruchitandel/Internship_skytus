# 1. Check Prime Number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 2. Reverse a String
def reverse_string(text):
    return text[::-1]


# 3. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


# 4. Simple Interest
def simple_interest(p, r, t):
    return (p * r * t) / 100


# 5. Palindrome Check
def is_palindrome(word):
    return word == word[::-1]


# 6. Count Vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


# 7. Merge Two Lists
def merge_lists(list1, list2):
    return list1 + list2


# 8. GCD of Two Numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 9. Area of Rectangle
def area_rectangle(length, width):
    return length * width


# 10. Armstrong Number Check
def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num



n = int(input("Enter a number to check Prime: "))
print("Prime:", is_prime(n))

text = input("Enter a string to reverse: ")
print("Reversed:", reverse_string(text))

num = int(input("Enter number for factorial: "))
print("Factorial:", factorial(num))

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
print("Simple Interest:", simple_interest(p, r, t))

word = input("Enter word to check palindrome: ")
print("Palindrome:", is_palindrome(word))

sentence = input("Enter string to count vowels: ")
print("Vowel Count:", count_vowels(sentence))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Merged List:", merge_lists(list1, list2))

a = int(input("Enter first number for GCD: "))
b = int(input("Enter second number for GCD: "))
print("GCD:", gcd(a, b))

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print("Area of Rectangle:", area_rectangle(length, width))

num = int(input("Enter number to check Armstrong: "))
print("Armstrong:", is_armstrong(num))

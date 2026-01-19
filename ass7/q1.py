# 1. Car Class
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print("Speed increased to:", self.speed)

    def brake(self, value):
        self.speed -= value
        print("Speed decreased to:", self.speed)


car = Car("Toyota", "Innova")
car.accelerate(30)
car.brake(10)


# 2. BankAccount Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.show_balance()


#  3. Student Class 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


student = Student("Ruchi", [80, 85, 90])
print("Average Marks:", student.average())


#  4. Rectangle Class 
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())


# 5. Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


emp = Employee("Amit", 50000)
emp.display()


#  6. Book Class 
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


book = Book("Python Basics", "Guido", 299)
book.display()


#  7. Circle Class 
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


circle = Circle(5)
print("Area:", circle.area())
print("Circumference:", circle.circumference())


#  8. Laptop Class 
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percent):
        discount = self.price * percent / 100
        self.price -= discount
        print("Price after discount:", self.price)


laptop = Laptop("Dell", 60000)
laptop.apply_discount(10)


#  9. Flight Class 
class Flight:
    def __init__(self, flight_no, seats):
        self.flight_no = flight_no
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked. Remaining seats:", self.seats)
        else:
            print("No seats available")


flight = Flight("AI202", 3)
flight.book_seat()
flight.book_seat()


# 10. Shop Class
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("Products in shop:")
        for p in self.products:
            print("-", p)


shop = Shop()
shop.add_product("Laptop")
shop.add_product("Mobile")
shop.show_products()

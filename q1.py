#  1. Animal  Dog, Cat 
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()


#  2. Vehicle  Car  ElectricCar 
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class ElectricCar(Car):
    def move(self):
        print("Electric car is running silently")

ev = ElectricCar()
ev.move()


#  3. Method Overriding 
class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):
    def show(self):
        print("This is child class")

obj = Child()
obj.show()


#  4. Multiple Inheritance 
class Father:
    def skill1(self):
        print("Father: Driving")

class Mother:
    def skill2(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Child: Coding")

c = Child()
c.skill1()
c.skill2()
c.skill3()


# ------------------ 5. Polymorphism Example ------------------
class Circle:
    def draw(self):
        print("Drawing Circle")

class Square:
    def draw(self):
        print("Drawing Square")

def draw_shape(shape):
    shape.draw()

draw_shape(Circle())
draw_shape(Square())


# ------------------ 6. Bank System ------------------
class BankAccount:
    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
        print("Savings Account Interest: 4%")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        print("Current Account Interest: 2%")

acc1 = SavingsAccount()
acc2 = CurrentAccount()
acc1.calculate_interest()
acc2.calculate_interest()


# ------------------ 7. Private Attributes + Getter/Setter ------------------
class Person:
    def __init__(self, name):
        self.__name = name   # private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

p = Person("Ruchi")
print("Name:", p.get_name())
p.set_name("Amit")
print("Updated Name:", p.get_name())


# ------------------ 8. Teacher → Student Inheritance ------------------
class Teacher:
    def teach(self):
        print("Teacher is teaching")

class Student(Teacher):
    def study(self):
        print("Student is studying")

s = Student()
s.teach()
s.study()


# ------------------ 9. MusicPlayer → Spotify Overriding ------------------
class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music from Spotify")

app = Spotify()
app.play()


# ------------------ 10. super() in Inheritance ------------------
class A:
    def __init__(self):
        print("Class A constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("Class B constructor")

obj = B()

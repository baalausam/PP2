#1. Class with getString and printString methods
class StringManipulator:
    def __init__(self):
        self.string = ""
        
    def getString(self):
        self.string = input("Enter a string: ")
    
    def printString(self):
        print(self.string.upper())
#2. Shape and Square Classes
class Shape:
    def __init__(self):
        self.name = "Shape"
    
    def area(self):
        return 0  # Default area for Shape

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.name = "Square"
    
    def area(self):
        return self.length ** 2  # Area of Square
#3. Rectangle Class (Inheriting from Shape)
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
        self.name = "Rectangle"
    
    def area(self):
        return self.length * self.width  # Area of Rectangle
#4. Point Class
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
#5. Account Class
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance for withdrawal.")
#6. Filtering Prime Numbers using filter and lambda
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 13, 16, 17]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Prime numbers:", prime_numbers)
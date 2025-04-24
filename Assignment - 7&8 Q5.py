import math
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

def user_input():
    print("Choose the shape to calculate area and perimeter:")
    print("1. Rectangle")
    print("2. Circle")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        rectangle = Rectangle(length, width)
        print(f"Rectangle - Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")

    elif choice == '2':
        radius = float(input("Enter the radius of the circle: "))
        circle = Circle(radius)
        print(f"Circle - Area: {circle.area()}, Perimeter: {circle.perimeter()}")

    else:
        print("Invalid choice, please enter 1 or 2.")

user_input()

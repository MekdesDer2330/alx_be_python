import math

class Shape:
    def area(self):
        """Method to calculate area; to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Initialize the rectangle's length and width."""
        self.length = length
        self.width = width

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        """Initialize the circle's radius."""
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()

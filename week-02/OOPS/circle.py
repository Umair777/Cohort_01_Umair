import math
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, radius, color = "red"):
        self.radius = radius
        self.color = color
    
    def add_radius(self, r):
        self.radius += r
        return (self.radius)
            
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), self.radius, color=self.color))
        plt.axis('scaled')
        plt.show()
        
# Example usage:
circle = Circle(5, "blue")
print("Initial Radius:", circle.radius)
circle.add_radius(3)
print("Updated Radius:", circle.radius)
print("Area of Circle:", circle.area())
circle.drawCircle()

'''
OUTPUT:
Initial Radius: 5
Updated Radius: 8
Area of Circle: 201.06192982974676'''
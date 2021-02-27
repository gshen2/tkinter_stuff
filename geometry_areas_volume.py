import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius**2
        return round(area, 2)

    def circumference(self):
        circumference = 2*math.pi*self.radius
        return round(circumference, 2)


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        volume = math.pi * self.radius**2 * self.height
        return round(volume, 2)

    def surface_area(self):
        surface_area = math.pi * self.radius**2 +\
            2 * self.radius * self.height
        return round(surface_area, 2)


# Testing codes
# print(circle(radius=3).circumference())
print(Cylinder(radius=3, height=2).surface_area())

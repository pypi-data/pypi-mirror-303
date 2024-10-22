from math import sqrt, pi

class Rocket():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        distance = sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2)
        return distance
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"A Rocket positioned at ({self.x}, {self.y})"

    def __repr__(self):
        return f"Rocket({self.x}, {self.y})"
    
class Shuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed

class CircleRocket(Rocket):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius
    
    def get_area(self):
        area = pi * self.radius**2
        return area
    
    def get_circumference(self):
        circumference = 2 * pi * self.radius
        return circumference
    
    def __str__(self):
        return f"A CircleRocket positioned at ({self.x}, {self.y}) with radius {self.radius}"
    
    def __repr__(self):
        return f"CircleRocket({self.x}, {self.y}, {self.radius})"

from math import sqrt, pi

class Rocket:
    # Rocket simulates a rocket ship for a game or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x, y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the parameters given.
        # Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculate the distance from this rocket to another rocket,
        # and return that value.
        distance = sqrt((self.x - other_rocket.x) ** 2 + (self.y - other_rocket.y) ** 2)
        return distance
    
    def __str__(self):
        return f"A Rocket positioned at ({self.x},{self.y})"

    def __repr__(self):
        return f"Rocket({self.x},{self.y})"
    
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


class Shuttle(Rocket):
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed


class CircleRocket(Rocket):
    
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)  
        self.radius = radius
    
    def get_area(self):
        return pi * (self.radius ** 2)
    
    def get_circumference(self):
        return 2 * pi * self.radius
    
    def __str__(self):
        return f"A CircleRocket positioned at ({self.x},{self.y}) with radius {self.radius}"

    def __repr__(self):
        return f"CircleRocket({self.x},{self.y}, radius={self.radius})"


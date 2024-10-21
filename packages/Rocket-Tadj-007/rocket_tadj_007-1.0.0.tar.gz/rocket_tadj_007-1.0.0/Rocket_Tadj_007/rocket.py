# rocket.py
from math import sqrt, pi

class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.
    
    def __init__(self, x=0, y=0):
        # Each rocket has an (x,y) position.
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the paremeters given.
        #  Default behavior is to move the rocket up one unit.
        self.x += x_increment
        self.y += y_increment
        
    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket,
        #  and returns that value.
        distance = sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
    
    def __eq__(self, other):
        if isinstance(other, Rocket):
            return self.x == other.x and self.y == other.y
        return False
    
    def __str__(self):
        return f"A Rocket positioned at ({self.x},{self.y})"

    def __repr__(self):
        return f"Rocket({self.x},{self.y})"
    
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    #  just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed

class CircleRocket(Rocket):
    # CircleRocket simulates a rocket shaped like a circle.
    
    def __init__(self, x=0, y=0, r=1):
        super().__init__(x, y)
        self.r = r
        
    def get_area(self):
        return pi * self.r ** 2
    
    def get_circumference(self):
        return 2 * pi * self.r
    
    def __str__(self):
        return f"A CircleRocket positioned at ({self.x},{self.y}) with radius {self.r}"
    
    def __repr__(self):
        return f"CircleRocket({self.x},{self.y}, radius={self.r})"

# Insert testing code here

# Importing the entire module
import rocket

rocket_0 = rocket.Rocket(10, 20)
print(rocket_0)
print("Rocket Distance Check:", rocket_0.get_distance(rocket.Rocket(30, 40)))

# Import specific class
from rocket import Shuttle

shuttle_0 = Shuttle(10, 20, 5)
print(shuttle_0)
print("Shuttle Distance Check:", shuttle_0.get_distance(rocket.Rocket(30, 40)))

# Import using aliasing
import rocket as r

rocket_1 = r.Rocket(50, 60)
print(rocket_1)
print("Rocket Equality Check:", rocket_0 == rocket_1)

# Test CircleRocket
from rocket import CircleRocket

circle_rocket = CircleRocket(10, 20, 5)
print(circle_rocket)
print(f"Area: {circle_rocket.get_area()}")
print(f"Circumference: {circle_rocket.get_circumference()}")
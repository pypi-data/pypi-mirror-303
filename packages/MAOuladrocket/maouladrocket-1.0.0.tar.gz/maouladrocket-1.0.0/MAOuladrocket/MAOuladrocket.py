from math import sqrt, pi

class Rocket():
    # Rocket simulates a rocket ship for a game,
    # or a physics simulation.
    
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
        # Calculates the distance from this rocket to another rocket,
        # and returns that value.
        distance = sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2)
        return distance
    
    def __str__(self):
        return f"A Rocket positioned at ({self.x}, {self.y})"

    def __repr__(self):
        return f"Rocket({self.x}, {self.y})"
        
    def __eq__(self, other):
        # Check if the other object is of the same type and has equal positions.
        if isinstance(other, type(self)):
            return (self.x == other.x) and (self.y == other.y)
        return False

        
class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is really
    # just a reusable rocket.
    
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed

    def __str__(self):
        return f"Shuttle(position=({self.x}, {self.y}), flights_completed={self.flights_completed})"

    def __eq__(self, other):
        # Use the parent equality check and add flights_completed check.
        if isinstance(other, Shuttle):
            return super().__eq__(other) and (self.flights_completed == other.flights_completed)
        return False


class CircleRocket(Rocket):
    # CircleRocket adds a circular shape to the Rocket.
    
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        # Calculate the area of the circle.
        return pi * (self.radius ** 2)
    
    def get_circumference(self):
        # Calculate the circumference of the circle.
        return 2 * pi * self.radius
    
    def __str__(self):
        return f"CircleRocket(position=({self.x}, {self.y}), radius={self.radius})"
    
    def __repr__(self):
        return f"CircleRocket({self.x}, {self.y}, radius={self.radius})"

    def __eq__(self, other):
        # Use the parent equality check and add radius comparison.
        if isinstance(other, CircleRocket):
            return super().__eq__(other) and (self.radius == other.radius)
        return False
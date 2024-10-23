from math import sqrt, pi


class Rocket:
    # Rocket simulates a rocket ship for a game or a physics simulation.

    def __init__(self, x=0, y=0):
        # Each rocket has an (x, y) position.
        self.x = x
        self.y = y

    def move_rocket(self, x_increment=0, y_increment=1):
        # Move the rocket according to the parameters given.
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        # Calculates the distance from this rocket to another rocket.
        return sqrt((self.x - other_rocket.x) ** 2 + (self.y - other_rocket.y) ** 2)

    def __eq__(self, other_rocket):
        # Checks if two rockets have the same position.
        return (self.x, self.y) == (other_rocket.x, other_rocket.y)

    def __str__(self):
        return f"A Rocket positioned at ({self.x}, {self.y})"

    def __repr__(self):
        return f"Rocket({self.x}, {self.y})"


class Shuttle(Rocket):
    # Shuttle simulates a space shuttle, which is a reusable rocket.

    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x, y)
        self.flights_completed = flights_completed

    def __str__(self):
        return f"A Shuttle positioned at ({self.x}, {self.y}) with {self.flights_completed} flights completed."

    def __repr__(self):
        return f"Shuttle({self.x}, {self.y}, flights_completed={self.flights_completed})"


class CircleRocket(Rocket):
    # CircleRocket models a rocket in the form of a circle with radius r.

    def __init__(self, x=0, y=0, r=1):
        super().__init__(x, y)
        self.r = r

    def get_area(self):
        # Calculates the area of the circle-shaped rocket.
        return pi * self.r**2

    def get_circumference(self):
        # Calculates the circumference of the circle-shaped rocket.
        return 2 * pi * self.r

    def __str__(self):
        return f"A CircleRocket positioned at ({self.x}, {self.y}) with radius {self.r}"

    def __repr__(self):
        return f"CircleRocket({self.x}, {self.y}, radius={self.r})"

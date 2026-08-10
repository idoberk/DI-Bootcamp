# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Object-Oriented Programming (OOP)
# Dunder (Magic) Methods in Python

# Instructions
# The goal is to create a class that represents a simple circle.

# A Circle can be defined by either specifying the radius or the diameter - use a decorator for it.
# The user can query the circle for either its radius or diameter.

# Abilities of a Circle Instance
# Your Circle class should be able to:

# ✅ Compute the circle’s area.
# ✅ Print the attributes of the circle — use a dunder method (__str__ or __repr__).
# ✅ Add two circles together and return a new circle with the new radius — use a dunder method (__add__).
# ✅ Compare two circles to see which is bigger — use a dunder method (__gt__).
# ✅ Compare two circles to check if they are equal — use a dunder method (__eq__).
# ✅ Store multiple circles in a list and sort them — implement __lt__ or other comparison methods.

# Bonus Challenge (Optional)
# If you want an extra challenge:

# Install the Turtle module (pip install PythonTurtle)
# Draw the sorted circles visually on the screen!

# 💡 Tip:

# Test your implementation by creating several circles and printing comparisons, additions, and sorted results.

from functools import total_ordering


@total_ordering
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return 3.14159 * self.radius**2

    @diameter.setter
    def diameter(self, value):
        if value <= 0:
            raise ValueError("Diameter can't be 0 or negative")
        self.radius = value / 2

    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        new_radius = self.radius + other.radius

        return Circle(new_radius)

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return self.area > other.area

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented

        return self.radius == other.radius

    def __str__(self):
        return f"Circle area: {round(self.area, 2)} --- Circle diameter: {round(self.diameter, 2)} --- Circle radius: {round(self.radius, 2)}"

    def __repr__(self):
        return f"Circle radius: {round(self.radius, 2)}"


circles = [
    Circle(50),
    Circle(70),
    Circle(20),
    Circle(40),
    Circle(10),
    Circle(120),
    Circle(30),
    Circle(40),
]

print(circles)

new_circle = circles[0] + circles[4]
print(new_circle)

sorted_circles = sorted(circles)
for circle in sorted_circles:
    print(circle)

# math_utils.py
"""Simple math utilities for examples."""

PI = 3.14159

def add(a, b):
    """Return a + b."""
    return a + b

def circle_area(radius):
    """Area of circle using module PI."""
    return PI * radius * radius

class Calculator:
    def multiply(self, a, b):
        return a * b

# code under this runs only when the file is executed directly
if __name__ == "__main2__":
    print("math_utils test run")
    print("add(2,3) =", add(2, 3))
    print("area r=2 ->", circle_area(2))

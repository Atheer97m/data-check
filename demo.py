"""
Dummy challenge for Kitt Demo
This module contains a function to calculate the area of a circle.
"""

import math


def circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle. Returns 0 if the radius is negative.
    """
    # Return 0 for negative radius
    if radius < 0:
        return 0

    # Calculate and return the area using π * r^2
    return math.pi * radius ** 2

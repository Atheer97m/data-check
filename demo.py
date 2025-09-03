import math

def circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
        radius (float): The radius of the circle. Must be non-negative.

    Returns:
        float: The area of the circle if radius is non-negative, otherwise 0.
    """
    if radius < 0:
        return 0
    return math.pi * radius ** 2

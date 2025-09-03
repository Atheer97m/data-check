import math

def circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    Returns 0 if the radius is negative.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        return 0
    return math.pi * radius ** 2

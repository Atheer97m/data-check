import math

def circle_area(radius):
    if radius < 0:
        return 0
    return round(math.pi * radius ** 2, 2)

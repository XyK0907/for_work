import math

class Point(object):
    """Represents a point in 2-D space."""


def distance_between_points(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


if __name__ == '__main__':
    a = Point()
    a.x = 3
    a.y = 4

    b = Point()
    b.x = 3
    b.y = 5
    print(distance_between_points(a, b))
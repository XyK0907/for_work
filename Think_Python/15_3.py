import copy
class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """


class Point(object):
    """Represents a point in 2-D space."""


def move_rectangle(rect, dx, dy):
    rect1 = copy.deepcopy(rect)

    rect1.corner.x += dx
    rect1.corner.y += dy
    return rect1


if __name__ == '__main__':
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    print(box.width)
    print(box.height)
    print(box.corner.x)
    print(box.corner.y)

    rect1 = move_rectangle(box, 3,3)
    print(box.corner.x)
    print(box.corner.y)
    print(rect1.corner.x)
    print(rect1.corner.y)
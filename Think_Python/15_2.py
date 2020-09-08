class Rectangle(object):
    """Represents a rectangle.

    attributes: width, height, corner.
    """


class Point(object):
    """Represents a point in 2-D space."""


def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy


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

    move_rectangle(box, 3,3)
    print(box.corner.x)
    print(box.corner.y)
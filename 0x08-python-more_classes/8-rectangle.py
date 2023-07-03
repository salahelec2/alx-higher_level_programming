#!/usr/bin/python3
"""the module containe Rectangle class

"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = Rectangle.print_symbol
        if (type(height) != int):
            raise TypeError("height must be an integer")
        elif (height < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if (type(width) != int):
            raise TypeError("width must be an integer")
        elif (width < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if (self.height == 0 or self.width == 0):
            return 0
        else:
            return 2 * self.height + 2 * self.width

    def __str__(self):
        if (self.height != 0 and self.width != 0):
            a = self.width * "{0!s}".format(self.print_symbol) + "\n"
            b = self.width * "{0!s}".format(self.print_symbol)
            return ((self.height - 1) * a + b)
        else:
            return ("")

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (isinstance(rect_1, Rectangle) is False):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif (isinstance(rect_2, Rectangle) is False):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif (rect_1.area() >= rect_2.area()):
            return(rect_1)
        else:
            return(rect_2)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

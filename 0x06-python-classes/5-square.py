#!/usr/bin/python3
"""CLASS SQUARE DEFINITION"""


class Square:
    """the square class body"""

    def __init__(self, size=0):
        """new Square init .
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the square."""
        return (self.__size ** 2)
    
    def my_print(self):
        """Prints the square."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

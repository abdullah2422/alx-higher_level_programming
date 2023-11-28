#!/usr/bin/python3
"""Defines a Rectangle class"""

class Rectangle:
    """A class Rectangle."""
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the width of the Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle instance."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        """Retrieves the height of the Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Retrieves the height of the Rectangle instance."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
             raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the Rectangle instance."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

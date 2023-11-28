#!/usr/bin/python3
"""Defines a Rectangle class"""

class Rectangle:
    """A class Rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """Retrieves the width of the Rectangle instance."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle instance."""
        if type(value) is not int:
            raise TypeError("must be an integer")
        elif value < 0:
             raise ValueError("with the message width must be >= 0")
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
            raise TypeError("must be an integer")
        elif value < 0:
            raise ValueError("with the message height must be >= 0")
        else:
            self.__height = value
            
    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.__width * self.__height
  
    def perimeter(self):
        """Returns the perimeter of the Rectangle instance."""
        if self.height != 0 or self.width != 0:
            perimeter = 0
        return 2 * (self.__width + self.__height)
    def __str__(self):
        """Returns a string representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width for _ in range(self.__height)])
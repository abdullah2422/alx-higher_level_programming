#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """A class Rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
        
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("must be an integer")
        elif value < 0:
             raise ValueError("with the message width must be >= 0")
        else:
            self.__width = value
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("must be an integer")
        elif value < 0:
             raise ValueError("with the message height must be >= 0")
        else:
            self.__height = value

#!/usr/bin/python3
from base import Base
''' class for our firs rectangle'''


class Rectangle(Base):




    def __init__(self,width, height, x=0, y=0, id=None):
        '''initializing Attributes for the object rectangle'''

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    
    @property
    def width(self):
        '''Getter to get the value of width'''
        return self._width


    @width.setter
    def width(self, width):
        '''Sets the value of width'''

        if type(width) != int:
            raise TypeError("Width must be an integer")
        if width<=0 :
            raise ValueError("Width must be >0")

        self._width = width


    @property
    def height(self):
        '''Gets the value of height'''

        return self._height


    @height.setter
    def height(self, height):
        '''Sets the value of height'''

        if type(height) != int:
            raise TypeError("Height must be an integer")

        if height<=0:
            raise ValueError("Height must be >0")
        self._height = height


    @property
    def x(self):
        '''Gets the value of x'''
        return self._x


    @x.setter
    def x(self, x):
        '''Sets the value of height'''

        if type(x) != int:
            raise TypeError("X must be positive")
        
        if x<0 :
            raise ValueError("X must be>=0")
        self._x = x

    
    @property
    def y(self):
        '''Gets the value of y'''

        return self._y


    def y(self, y):
        '''Sets the value of y'''

        if y!=int :
            raise TypeError("Y must be an int")

        if y<0:
            raise ValueError("y must be>0")
        self._y = y


    def area(self):
        '''calculates the area of the rectangle'''
        return self._height * self._width
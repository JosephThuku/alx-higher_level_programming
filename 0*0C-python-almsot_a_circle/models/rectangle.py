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
        self._width = width


    @property
    def height(self):
        '''Gets the value of height'''

        return self._height


    @height.setter
    def height(self, height):
        '''Sets the value of height'''
        self._height = height


    @property
    def x(self):
        '''Gets the value of x'''
        return self._x


    @x.setter
    def x(self, x):
        '''Sets the value of height'''
        self._x = x

    
    @property
    def y(self):
        '''Gets the value of y'''

        return self._y


    def y(self, y):
        '''Sets the value of y'''

        self._y = y
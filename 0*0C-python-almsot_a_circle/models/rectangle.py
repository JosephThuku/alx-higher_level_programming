#!/usr/bin/python3
from models.base import Base
''' class for our firs rectangle'''


class Rectangle(Base):



    def __init__(self,width, height,x=0,y=0,id=None):
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
            raise TypeError("X must be an integer")
        
        if x<0 :
            raise ValueError("X must be>=0")
        self._x = x

    
    @property
    def y(self):
        '''Gets the value of y'''

        return self._y

    @y.setter
    def y(self, y):
        '''Sets the value of y'''

        if type(y)!=int:
            raise TypeError("Y must be an int")

        if y<0:
            raise ValueError("y must be>0")
        self._y = y


    def area(self):
        '''calculates the area of the rectangle'''
        return self._height * self._width


    def display(self):
        '''Display the rectangle using #'''
        for y in range(self.y):
            print("")

        for row in range(self._height):
            for x in range(self.x):
                print("", end="")

            for d in range(self._width):
                print("#", end="")
            
            print()
    def __str__(self):
        return f"[Rectangle]({self.id}) ({self._x}) ({self.y})/ ({self._width}) /({self._height})"


    def update(self, *args, **kwargs):
        '''assigns an argument all the atttributes'''
        if args:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]

        else:
            ''' checks if the attribute has a value if not assign a key and value'''
            for key, value in kwargs.items():
                setattr(self, key, value)
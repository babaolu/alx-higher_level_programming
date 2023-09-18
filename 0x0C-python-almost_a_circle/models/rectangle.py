#!/usr/bin/python3
""" This implements the Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization function """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > zero")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > zero")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= zero")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= zero")
        self.__y = y

    def area(self):
        """ Returns the area of this Rectangle """
        return self.width * self.height

    def display(self):
        """ Prints # representation of rectangle """
        for i in range(self.y):
            print("")
        print((self.height-1) * (" " * self.x + self.width * "#" + "\n")
              + " " * self.x + self.width * "#")

    def __str__(self):
        """ Return informal string description of Rectangle object """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Updates the attributes of a rectangle """
        if args is None or not args:
            if kwargs:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value
            return
        if len(args) > 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        elif len(args) == 4:
            self.id, self.width, self.height, self.x = args
        elif len(args) == 3:
            self.id, self.width, self.height = args
        elif len(args) == 2:
            self.id, self.width = args
        else:
            [self.id] = args

    def to_dictionary(self):
        """ Returns dictionary representation of Rectangle object """
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["width"] = self.width
        my_dict["height"] = self.height
        my_dict["x"] = self.x
        my_dict["y"] = self.y
        return my_dict

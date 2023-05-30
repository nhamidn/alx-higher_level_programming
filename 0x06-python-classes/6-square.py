#!/usr/bin/python3
class Square:
    """A class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """Method that calculate the area of the square"""
        return self.__size * self.__size

    @property
    def size(self):
        """Getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of __size"""
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Square printer using # and space"""
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print("")

    @property
    def position(self):
        """Getter of __position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of __position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

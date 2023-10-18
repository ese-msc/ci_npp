""" This module contains the classes for some simple shapes."""

import numpy as np


__all__ = ['Rectangle', 'Square', 'Circle', 'Triangle',
           'ratio_area_perimeter', 'ratio_area_mean_side',
           'ratio_perimeter_mean_side']


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def mean_side(self):
        return (self.width + self.height)/2

    def perimeter(self):
        return (self.width + self.height)


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def area(self):
        return super().area()

    def mean_side(self):
        return self.side

    def perimeter(self):
        return 4*self.side


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return np.pi*self.radius**2

    def mean_side(self):
        return 2*self.radius

    def perimeter(self):
        return 2*np.pi*self.radius


class Triangle:

    def __init__(self, side1, side2, side3):

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3)/2
        return np.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))

    def mean_side(self):
        return (self.side1 + self.side2 + self.side3)/3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


def ratio_area_perimeter(shape):
    return shape.area()/shape.perimeter()


def ratio_area_mean_side(shape):
    return shape.area()/shape.mean_side()


def ratio_perimeter_mean_side(shape):
    return shape.perimeter()/shape.mean_side()

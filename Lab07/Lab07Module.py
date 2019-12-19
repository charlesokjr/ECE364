#######################################################
#    Author:      <Ethan Glaser>
#    email:       <glasere@purdue.edu>
#    ID:           <ee364a13>
#    Date:         <10/15/19>
#######################################################
import os
import math
#######################################################
# No Module -Level  Variables  or  Statements!
# ONLY  CLASSES  AND  FUNCTIONS  BEYOND  THIS  POINT!
#######################################################


class Rectangle:
    def __init__(self, llpoint, urpoint):
        xll, yll = llpoint
        xur, yur = urpoint
        if xur < xll or yur < yll:
            raise ValueError("Invalid coordinates: the x and y coordinates in the lower left"
                             " point must be greater than the upper right point")
        self.lowerLeft = llpoint
        self.upperRight = urpoint

    def isSquare(self):
        xll, yll = self.lowerLeft
        xur, yur = self.upperRight
        if xur - xll == yur - yll:
            return True
        else:
            return False

    def intersectsWith(self, rect):
        xll, yll = self.lowerLeft
        xur, yur = self.upperRight
        xllRect, yllRect = rect.lowerLeft
        xurRect, yurRect = rect.upperRight
        for x in [xur, xll]:
            for y in [yur, yll]:
                if xllRect < x < xurRect and yllRect < y < yurRect:
                    return True
        return False

    def __eq__(self, other):
        if type(other) != Rectangle:
            raise ValueError("Input Error: must be of class Rectangle")
        xll, yll = self.lowerLeft
        xur, yur = self.upperRight
        xllRect, yllRect = other.lowerLeft
        xurRect, yurRect = other.upperRight
        if (xur - xll) * (yur - yll) == (xurRect - xllRect) * (yurRect - yllRect):
            return True
        else:
            return False


class Circle:
    def __init__(self, c, r):
        if r <= 0:
            raise ValueError('Input Error: Radius must be greater than 0')
        self.center = c
        self.radius = r

    def intersectsWith(self, other):
        if type(other) == Circle:
            x, y = self.center
            xx, yy = other.center
            dist = math.sqrt((xx - x) ** 2 + (yy - y) ** 2)
            if dist < self.radius + other.radius:
                return True
            return False
        elif type(other) == Rectangle:
            x1, y1 = other.lowerLeft
            x2, y2 = other.upperRight
            xc, yc = self.center
            for x in [x1, x2]:
                for y in [y1, y2]:
                    if self.radius > math.sqrt((x - xc) ** 2 + (y - yc) ** 2):
                        return True
                    elif (self.radius > x - xc and y1 < yc < y2) or (self.radius > y - yc and x1 < xc < x2):
                        return True
            return False
        else:
            raise ValueError("Input Error: Must be type Circle or Rectangle")


# This  block  is  optional  and  can be used  for  testing.
# We will  NOT  look  into  its  content.
#######################################################
if __name__ == "__main__":
    rect1 = Rectangle((-10,-10), (11,9))
    rect2 = Rectangle((1, 3), (5, 4))
    print(rect1.isSquare())
    print(rect2.isSquare())
    print(rect2.intersectsWith(rect1))
    print(rect1 == rect2)
    circ1 = Circle((0, 0), 5)
    circ2 = Circle((10,10), 10)
    rect3 = Rectangle((-4, -4), (-3.9, -3.9))
    print(circ1.intersectsWith(rect3))
    print(rect1.intersectsWith(rect3))
    print(circ1.radius)

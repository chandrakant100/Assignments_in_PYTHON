'To find the area of the triangle'

import math

print ("-----Enter the sides of the triangle-----")

side1 = float(input("Enter the side1:"))
side2 = float(input("Enter the side2:"))
side3 = float(input("Enter the side3:"))

s = (side1 +side2 + side3) /2
Area = math.sqrt(s*(s-1)*(s-2)*(s-3))

print ("\nArea = ",Area)
print ("\nArea after rounding the figure = ",round(Area,2))

"""print ("\nArea without floating points = ",math.trunc(Area))
print ("\nArea with higest integer precision = ",math.ceil(Area))
print ("\nArea with lowest integer precision = ",math.floor(Area))
"""

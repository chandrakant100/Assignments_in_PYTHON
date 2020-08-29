'Find the radius of the circle whose area = area of rectrangle'

import math

print ("Enter the length and breadth of the rectrange:\n")

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

AreaR = 2 * (length + breadth)

radius = math.sqrt(AreaR / 3.14)

print ("The radius of the circle whose area = rectrangle area is :",round(radius,2))
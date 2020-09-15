"""To find the roots of the quadratic eqation"""

import math

print ("Eqation format:\nax^2 + bx +c")

print ("Enter a,b,c respectively:\n")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b * b) - (4 * a * c)

if (a==0 and b==0):
    print ("\nRoots are not possible!!!")

elif (a == 0):
    print("\nThe equation has one root that is :",round((-c/b),2)) 

elif(d == 0):
    print ("\nThe eqauation has only one root:\n")
    root = (-b + math.sqrt(d)) / 2*a
    print ("Root: ",root)  

elif (d > 0):
        root1 = (-b + math.sqrt(d)) / 2*a
        root2 = (-b - math.sqrt(d)) / 2*a
        print("\nThe Equation has two roots:\n")
        print("\nRoot 1:",round(root1,1),"\nRoot 2:",round(root2,1))

else:
    print ("\nThe equation has two imaginary roots!!!")  

    
    


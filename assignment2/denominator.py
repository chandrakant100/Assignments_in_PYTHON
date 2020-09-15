#To check the denominator
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))
d = float(input("Enter the value of d: "))

if (c-d) == 0.5:
    print ("\nInvalid!!! Denominator is 0.5")
else:
    x = (a-b)/(c-d)
    print ("\nAfter Division value is ",round(x,2))    
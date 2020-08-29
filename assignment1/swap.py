'swapping two numbers without using third variable'

print ("Enter two numbers:\n")

num1 = float(input("Enter the number 1: "))
num2 = float(input("Enter the number 2: "))

print ("before swapping num1=",num1, "num2=",num2)

num1 = num1 +num2
num2 = num1 - num2
num1 = num1 - num2

print ("After swapping num1=",num1, "num2=",num2)


 
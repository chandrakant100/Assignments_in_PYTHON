#To arrange numbers in decending order

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
num3 = float(input("Enter num3: "))

print("Numbers in decending order are:\n")

if num1 > num2 and num1 > num3:
    print (num1," ")
    if num2 > num3:
        print(num2," ")
        print(num3," ")
    else:
        print(num3," ")
        print(num2," ")

elif num2 > num1 and num2 > num3:
    print (num2," ")
    if num1 > num3:
        print(num1," ")
        print(num3," ")
    else:
        print(num3," ")
        print(num1," ")

elif num3 > num1 and num3 > num2:
    print (num3," ")
    if num2 > num1:
        print(num2," ")
        print(num1," ")
    else:
        print(num1," ")
        print(num2," ")



    

#To check the divisiblity of a number
num = int (input("Enter a number: "))

if (num % 11 == 0 and num % 13 == 0) or (num % 5 ==0 and num % 7 == 0):
    print("The number ",num," is Divisible")
else:
    print("The number ",num," is not Divisible")
        

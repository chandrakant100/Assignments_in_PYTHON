#To round the number to nearest integer without using ceil() and floor()

num = float(input("Enter the floating value: "))

temp = int(num)

if num > 0:
    if (num == temp + 0.5):
        print ("Operation not posible: Atleast 2 decimal points required!!!")

    elif (num < temp + 0.5):
        print("Floor operation: ",temp)

    else:
        print("Ceil operation: ",temp+1)
else:
    print ("The number ",num," is nagative!!")


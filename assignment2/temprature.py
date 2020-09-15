num = int(input("Enter the reading: "))

if num ==2 or num ==3:
    temprature = 500
elif num == 4:
    temprature = 600
elif num ==5 or num ==6 or num == 7:
    temprature = 700
else:
    temprature = 300

print ("The temprature of the oven is ",temprature,"degrees")    

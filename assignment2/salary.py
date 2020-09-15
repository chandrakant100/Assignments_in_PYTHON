""" calculate the Gross salary of an employee"""

Bsalary = float(input("Enter your Basic salary: "))

DA = 0.6 * Bsalary
HRA = 0.15 * Bsalary
Conveyance = 0.15 * Bsalary
Medical = 0.1 * Bsalary

Gsalary = Bsalary + DA +Conveyance + Medical

print ("\nBasic Salary    = ",round(Bsalary,2))
print ("DA              = ",round(DA))
print ("HRA             = ",round(HRA))
print ("Conveyance      = ",round(Conveyance))
print ("Medical         = ",round(Medical))
print ("\nGross Salary  = ",round(Gsalary))







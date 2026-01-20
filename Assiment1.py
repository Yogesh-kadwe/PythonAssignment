name=input("Enter your name: ")
emp_id=input("Enter your employee ID: ")
deperment=input("Enter your department: ")
basic_salary=float(input("Enter your basic salary: "))

hra=0.92*basic_salary
da=0.58*basic_salary
ta=0.30*basic_salary
lic=500
gross_salary=basic_salary+hra+da+ta
net_salary= gross_salary - lic
print("Salary details of employee:")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", deperment)
print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("TA:", ta)
print("LIC Deduction:", lic)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)
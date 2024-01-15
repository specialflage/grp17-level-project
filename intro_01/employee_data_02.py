employee_id = 101                   #int
employee_name = "Mohamed Aasem"     #str
employee_job = "Python Developer"   #str
employee_salary = 7000.55           #float


print("------------------------------Concatenation with a string ------------------------------")
print(employee_name + " " + "works as" + " a " + employee_job)
print("------------------------------Concatenation with a int ------------------------------")
# convert data type from int to string : casting
print(employee_name + " " + "has ID " + str(employee_id))
print(employee_name + "takes salary" + str(employee_salary) )
print("------------------------------Casting from float to int [ to remove decimal ]------------------------------")
print(employee_salary)
print( int(employee_salary))

emp_sal = 4000
print(float(emp_sal))

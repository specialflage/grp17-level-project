company_employees = [
(101, 'Ahmed Esam', 10000.0, 'Cairo'),
(102, 'Ibrahim Ahmed', 9000.0, 'Cairo'),
(103, 'Adham Aly', 5000.0, 'Cairo'),
(104, 'Islam Hasan', 7000.0, 'Cairo')
]

tot_salr = sum(emplyee[2] for emplyee in company_employees)
print(tot_salr)
'''
for employee in company_employees:
    employee_salary = employee[2]
    for employee_salary in company_employees:
        counter = employee_salary
        sum_employee_salary = employee_salary + counter
    print(sum_employee_salary)
'''
sum_salary = 0
for employee in company_employees:
    emp_ID, emp_Name, emp_Salary, emp_Location = employee
    sum_salary = emp_Salary + sum_salary
print(sum_salary)

company_employees = [
(101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
(102, 'Ibrahim Ahmed', 9000.0, 'Accountant','M'),
(103, 'Adham Aly', 5000.0, 'Engineer', 'M'),
(104, 'Islam Hasan', 7000.0, 'Sales', 'M'),
(104, 'Marwa Esam', 7000.0, 'Marketer', 'F'),
(104, 'Ola Hasan', 7000.0, 'Engineer', 'F')
]
sum_f = 0
sum_m = 0

for employee in company_employees:
    emp_ID, emp_Name, emp_Salary, emp_job, emp_Gender = employee
    if emp_Gender == 'F':
        sum_f = sum_f + 1
    elif emp_Gender == 'M':
        sum_m = sum_m + 1
print('\n Female Count: ', sum_f, '\n Male Count: ', sum_m)



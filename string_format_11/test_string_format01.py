#show all printing options
import math

emp_id = 101
emp_name = 'Esam omar'
emp_salary = 7853453.6782123
print('------1. Print with concat------')
print('Emps has id = ' +str(emp_id) + ', his name is ' + emp_name + '\n\ttakes salary = ' + str(emp_salary))

print('---------------2. Print with multiple parameters-------------')
print('Emps has id = ', (emp_id), ', his name is ',  emp_name, '\n\ttakes salary = ', (emp_salary))


print(150, 120, 200, 30, sep='-')
for i in range(11):
    print(i, end=' ')
print('test')
print('\ntest1')
print('test2')

print('--------3. String formating using placeholders-----%s %d %f--------')
print('Emp has id = %d, his name is %s, takes salary = %f' %(emp_id, emp_name, emp_salary))

print('--------4. String formating using format Function-------------')
print('Emp has id = {}, his name is {}, takes salary = {}' .format(emp_id, emp_name, emp_salary))
print('Emp has id = {:d}, his name is {:s}, takes salary = {:,.2f}' .format(emp_id, emp_name, emp_salary))

print('--------5. String formating using F-string Function-------------')
print(F'Emp has id = {emp_id}, his name is {emp_name}, takes salary = {emp_salary: ,.2f}')

print('---------Numbers functions:      round, math.trunc, math.ceil, math.floor---------')
print(f'Using round function, result= {round(emp_salary, 2)}')
print(F'Using round function, result= {round(emp_salary, 2)}')
print(math.trunc(emp_salary))
print(math.ceil(emp_salary))
print(math.floor(emp_salary))

print(f'Using round function, result= {round(emp_salary, 2)
+++++++++++++++++++}')
print(f'Using trunc function, result= {math.trunc(emp_salary)}')
print(f'Using ceil function, result= {math.ceil(emp_salary)}')
print(f'Using floor function, result= {math.floor(emp_salary)}')
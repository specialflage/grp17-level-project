emp_name = ("Yahia Momtaz")
emp_gross_salary = 4000

if emp_gross_salary >= 5000:
    tax_pct = 10
else:
    tax_pct = 0
emp_net_salary = emp_gross_salary -tax_pct / 100 * emp_gross_salary
print("Emp net salary = " , emp_net_salary)

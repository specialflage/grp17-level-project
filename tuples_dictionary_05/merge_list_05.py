# Ex No. 1 : #  Merge 2 Lists into a single Dictionary with key values

emp_ids_list = [101, 102, 103]
emp_names_list = ['Ahmed', 'Omar', 'Sarah']

# Solution : {101: 'Ahmed', 102:'Omar', 103:'Sarah' }
person_dict = {}
# person_dic[101] = 'Ahmed'
# person_dic[102] = 'Omar'
# person_dic[103] = 'Sarah'

for i in range(len(emp_ids_list)):
    person_dict[ emp_ids_list[i]] = emp_names_list[i]

print(person_dict)
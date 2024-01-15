# Program to write a list to excel file
import csv

people_list = [
    ['Name', "Age", 'City'],
    ['Adham', '25', 'Assuit'],
    ['Essam', '30', 'Cairo'],
    ['Shady', '28', 'Ansoura']
]

with open('c:\\MY_FILES PYTHON\\people.csv', 'w', newline='') as my_file:
    w = csv.writer(my_file)
    for people in people_list:
        w.writerow(people)

    #w.writerow(['Name', "Age", 'City'])
    #w.writerow(['Adham', '25', 'Assuit'])
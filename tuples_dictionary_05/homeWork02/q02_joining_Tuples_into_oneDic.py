person_1_tuples = (101, "Ahmed Esam", 5000.0, "Cairo", "0127454184")
person_2_tuples = (102, "Mohamed Omar", 6000.0, "Alex", "01147041564")
person_3_tuples = (103, "Ibrahim Hesham", 7000.0, "Portsaid", "01032659878")

person1 = person_1_tuples[0]
person2 = person_2_tuples[0]
person3 = person_3_tuples[0]

personal_dic = {person1: person_1_tuples, person2: person_2_tuples, person3: person_3_tuples}
print("\n--------printing the three tuples into one dictionary ***  HOMEWORK  ***---------\n")
print(personal_dic)

print("\n----------Printing the resulted dictionary in three lines after defining each index of it ---------\n")

person1 = {"ID" : person_1_tuples[0], "Name": person_1_tuples[1], "Salary": person_1_tuples[2], "City": person_1_tuples[3], "Phone Number": person_1_tuples[4]}
person2 = {"ID" : person_2_tuples[0], "Name": person_2_tuples[1], "Salary": person_2_tuples[2], "City": person_2_tuples[3], "Phone Number": person_2_tuples[4]}
person3 = {"ID" : person_3_tuples[0], "Name": person_3_tuples[1], "Salary": person_3_tuples[2], "City": person_3_tuples[3], "Phone Number": person_3_tuples[4]}

personal = {"person1":(person1), "person2":(person2), "person3":(person3)}
for key, value in personal.items():
    print(f"{key}: {value}")
print("\n-----------Printing the dictionary the same above dictionary after defining its indexes into one line ------------\n")
print(personal)




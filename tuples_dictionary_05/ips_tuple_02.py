# program to show a list of Tuples

ips_list = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.11', 'y')
]

print('-----second element from the list index 1------')
print(ips_list[1])
print('------second element from list index1, y or no ------')
print(ips_list[1][1])
print('----------print all ips that are y-------')

'''
for item in ips_list:
    if item [1] == 'y':
        print(item)
'''
for i in range(len(ips_list)):
    if ips_list[i][1] == 'y':
        print(ips_list[i])


print('------task : print the last part of the yes ip in the last loop -------')
'''
('192.168.0.15', 'y') 15
('192.168.0.22', 'y') 22
('192.168.0.14', 'y') 14
('192.168.0.11', 'y') 11
'''
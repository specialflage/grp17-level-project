# Program to write into text file
'''
1. open for write
2. write
3. close
'''
print('----------first way-------')

my_file = open('C:\\MY_FILES PYTHON\\write_data.txt', 'w')
my_file.write('I like programming\n')
my_file.write('I like football\n')
my_file.write('Python is a programming Language\n')
my_file.close()

print('----- second way ------- using with -------')
with open('C:\\MY_FILES PYTHON\\write_data.txt', 'w') as my_file:
    my_file.write('\n')
    my_file.write('My city is Cairo\n')
    my_file.write('My City is aLex\n')
    my_file.write('')

with open('C:\\MY_FILES PYTHON\\write_data.txt', 'a') as my_file:
        my_file.write('\n')
        my_file.write('My city is Cairo\n')
        my_file.write('My City is aLex\n')
        my_file.write('')
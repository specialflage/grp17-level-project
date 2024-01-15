#Find if a number is found in a list- print its first index
# or print.. number is not found using a flag
my_list = [14, 5, 22, 10, 30]
num = 24

is_found = False
for item in my_list:
    if item == num:
        print('No is not found', my_list.index(item))
        is_found = True

if is_found == False:
    print('Nu. is not found')
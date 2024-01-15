#Find if a number is found in a list- print its first index
# or print.. number is not found using a Else loop
my_list = [14, 5, 22, 10, 30]
num = 24
for item in my_list:
    if num == item:
        print('number is found at index = ', my_list.index(num))
        break
else:
        print('no is not found')
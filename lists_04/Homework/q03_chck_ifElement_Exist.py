# program to search for item in a list or not - if found print its index
# if not found : print it is not found in the list
'''
newList = [1, 6, 3, 5, 3, 4]
print("\nEnter the number you are locking for in the list\n")
userNum = input()

for i in newList:
    if i == userNum:
        print(userNum, " is found in index: ", i)
    elif i != userNum:
        print(userNum, "is not found in the list")

print("\nEnter a new number which you are locking for in the list\n")
userNum = input()

# else:
# print(userNum, "is not found in the list")

# if i == userNum:
# print(userNum, "is found in index: ", i)
# for i in newList:
# if i != userNum:
# print(userNum," is not found in the list")
'''
my_list = [14, 5, 2, 3, 7, 8, 2, 9, 7, 12, 2]
num= 7
indexes_list = []
is_found = False

for i in range(len(my_list)):
    if num == my_list[i]:
        is_found = True #flag
        required_index = i
        indexes_list.append(i)
        #break



if is_found == True:

       # print('it is found in the list at index =', required_index)
       print('it is found in the list at index =', indexes_list)
else:
        print('It is not found in the list')
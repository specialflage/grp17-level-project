# program to show nested lists
my_nested_list = [[101, 'ahmed', 'Cairo'], [102, 'mostafa', 'Alex']]
print(my_nested_list)
print(my_nested_list[0]) # [101, 'ahmed', 'Cairo']
print(my_nested_list[0][2]) # cairo

my_nested_list = \
    [[101, 'ahmed', ['Cairo', 'Nasr city', 'Makram ebeid']], [102, 'mostafa', 'Alex']]
print(my_nested_list[0][2][2]) # Makram Ebied
print("------=-=-=-=-=-=-=-=-=-==------")
newList = [12, 35, 9, 56, 24]
print(newList)
temp = newList[0]	# 12
newList[0] = newList[-1] # 24
newList[-1] = temp

print(newList)
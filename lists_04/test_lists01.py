# Using Lists
print(" ---- Creating, Printing List ---- ")
numbers_list = [7, 12, 8, 20, 9, 14]
print(numbers_list)
print(type(numbers_list))

print("2. adding element to the list [append function | insert function]")
numbers_list.append(11)
numbers_list.insert(1, 77)
print(numbers_list)
print(" ---- 3. Access element by index and change it ----")
print(numbers_list[4])
numbers_list[4] = 22 # change it
print(numbers_list)

# --------------------print(/n)

print("---4. count  elements of list _ Len function : General Function ----")
print(len(numbers_list))


print("----5. delet element from the list -- remove, pop functionss ----")
numbers_list.remove(9) # delete element 9
print(numbers_list)

numbers_list.pop(4) # delete at index 4 = 22 # numbers_list.pop() : remove last element
print(numbers_list)


print("------ 6. reverse list ------")
numbers_list.reverse()
print(numbers_list)


print("----- 7. sort list ------")
numbers_list.sort(reverse= True)
print(numbers_list)

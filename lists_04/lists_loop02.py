print("----1.For i loop ----")
numbers_list = [7, 12, 8, 20, 9, 14, 9]

#use index
sum_list = 0

for i in range(len(numbers_list)):
    print(i, numbers_list[i])
    sum_list = sum_list + numbers_list[i]

print("Sum of element =", sum_list)




print("----- 2. For each loop [ for in  loop ] : donot use list index -----")
sum_list = 0 # reset variable

for item in numbers_list:
    print(item)
    sum_list = sum_list + item
print("Sum of the element= ", sum_list)

print("===========using general function sum()========== ")
print(sum(numbers_list))

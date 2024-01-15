def sum_positive_numbers(numbers):

    return sum(num for num in numbers if num > 0)

def count_positive_numbers(numbers):

    return sum(1 for num in numbers if num > 0)


numbers_list = [1, -2, 3, 4, -5, 6]
sum_result = sum_positive_numbers(numbers_list)
count_result = count_positive_numbers(numbers_list)

print(f"The sum of positive numbers in the list is: {sum_result}")
print(f"The number of positive numbers in the list is: {count_result}")

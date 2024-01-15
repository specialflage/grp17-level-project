def find_max_min(numbers):
    max_num = min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num


numbers_sequence = [746, 289, 239, 693, 365, 146, 965, 315, 641, 645, 345]
max_number, min_number = find_max_min(numbers_sequence)

print(f"Maximum number: {max_number}")
print(f"Minimum number: {min_number}")
def get_min_num(nums):
    if not nums:
        # Return an appropriate value or raise an exception for an empty list
        return None

    # Initialize min_num with the first element of the list
    min_num = nums[0]

    # Iterate through the list to find the minimum number
    for num in nums:
        if num < min_num:
            min_num = num

    return min_num


def get_max_num(nums):
    if not nums:
        # Return an appropriate value or raise an exception for an empty list
        return None

    # Initialize max_num with the first element of the list
    max_num = nums[0]

    # Iterate through the list to find the maximum number
    for num in nums:
        if num > max_num:
            max_num = num

    return max_num


# Example usage:
numbers = [4, -7, 1, -9, 3, 11, -5]

min_result = get_min_num(numbers)
max_result = get_max_num(numbers)

print("The minimum number is:", min_result)
print("The maximum number is:", max_result)

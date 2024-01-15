# Initialize an empty list to store the results
result_numbers = []

# Iterate through the range from 1500 to 2701 (2701 is used to include 2700)
for number in range(1500, 2701):
    # Check if the number is divisible by 7 and a multiple of 5
    if number % 7 == 0 and number % 5 == 0:
        # If true, add the number to the result list
        result_numbers.append(number)

# Print the result list
print("Numbers between 1500 and 2700 that are divisible by 7 and multiples of 5:")
print(result_numbers)

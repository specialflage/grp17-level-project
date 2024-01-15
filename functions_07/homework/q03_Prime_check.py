def is_prime(number):
    """Check if a number is a prime number."""
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

# Take user input for a number
user_input = input("Enter a number to check if it's prime: ")

# Validate if the input is a positive integer
try:
    user_number = int(user_input)
    if user_number < 0:
        raise ValueError("Please enter a non-negative integer.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()

# Check if the entered number is prime
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")

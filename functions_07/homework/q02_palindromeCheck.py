def is_palindrome(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()

    # Remove spaces from the string
    s = ''.join(s.split())

    # Check if the string is equal to its reverse
    if s == s[::-1]:
        print(f'The word "{s}" is a palindrome: True')
        return True
    else:
        print(f'The word "{s}" is not a palindrome: False')
        return False


# Example usage:
str_example = 'radarkkj'
result = is_palindrome(str_example)

'''
def is_palindrome(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()

    # Remove spaces from the string
    s = ''.join(s.split())

    # Compare the string with its reverse
    return s == s[::-1]


# Example usage:
str_example = 'radaryu'
result = is_palindrome(str_example)
print(result)


'''
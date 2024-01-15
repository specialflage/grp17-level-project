str1 = '12521'
str2 = '123521'

# Remove spaces
str1 = ''.join(str1.split())
str2 = ''.join(str2.split())

# Check if the string is equal to its reverse
if str1 == str1[::-1]:
    print(f"{str1} is a palindrome")
else:
    print(f"{str1} is not a palindrome")

if str2 == str2[::-1]:
    print(f"{str2} is a palindrome")
else:
    print(f"{str2} is not a palindrome")

# to show how to handle exceptions
#import sys
try:
    first_number = int(input('Please Enter first number: '))
    second_number = int(input('Please enter second number: '))

    result = first_number + second_number
    print('Result = ', result)
except ValueError:
    print('Please enter only numbers.')
#    sys.exit()

print('Continue the program or end it...!')

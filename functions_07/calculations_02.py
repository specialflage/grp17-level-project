#Create 4 functions:
# 1. sum_numbers with 2 parameters : return result of adding these numbers
# 2. multiply_numbers with 3 parameters : return the result of multiplying these numbers
# 3. abs_numbers with 1 parameter : check if the numbers is -ve : return the +ve value
# 4. divid_numbers with 2 parameters : return the result of division
#    check the second number is not zero
print(' ------------------------Program 1------------------------')
def sum_numbers(x, y):
    sum = x + y
    return sum

# main program
res = sum_numbers(5, 3)
print(res)
print(' ------------------------Program 2------------------------')
def multiply_numbers(x, y, z):
    mul = x * y * z
    return mul
# Main 2
mul = multiply_numbers(2, 3, 4)
print(mul)
print(' ------------------------Program 3------------------------')
def abs_numbers(x):
    if x < 0:
        abs = x * -1
        return abs
    elif x == 0:
        print("It's neutral Zero")
    else:
        abs = x
        return abs
#main
abs1 = abs_numbers(0)
print(abs1)

print(' ------------------------Program 4------------------------')


def divid_numbers(x, y):
    if y == 0:
        print('not valid denominator')
    else:
        div = x / y
        return div
#Main 4
div1 = divid_numbers(8, 0)
print(div1)
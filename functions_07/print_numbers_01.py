# use functions print_numbers() : to print numbers from 1 to spesific num
# User Defined Function - Sub Program
def print_numbers(max_num):
    sum = 0
    for i in range(1, max_num+1):
        print(i, end= " ")
        sum = sum + i
    print()
    return sum

# main program
print("start program")
# Calling function : to print numbers 1: 10

z = print_numbers(10)
print(z)






print('End main program')
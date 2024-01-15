# program to calculate perimeter and area of circle
# inputs
import math

radius = 7
pi = 3.145

# area
# pow builtin function in the builtin math module

area = math.pi * math.pow(radius, 2)
area = round(area, 2)
print(area)
print('------------------------------------- Perimeter -------------------------------------')
perimeter = 2 * math.pi * radius
perimeter= round(perimeter, 2)
print(perimeter)

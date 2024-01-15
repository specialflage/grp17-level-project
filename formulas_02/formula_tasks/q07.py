import math

a = 1
b = 5
c = 2

part1 = math.sqrt(math.pow(b, 2) - (4 * a * c))
result = (part1 - b) / (2 * a)
print('')
print(result)
print('--OR--')
result = round(result, 2)
print(result)

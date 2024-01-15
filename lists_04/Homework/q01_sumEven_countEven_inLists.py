numList = [15, 16, 20, 3, 9, 20]
sumEven, sumOdd, countEven, countOdd = 0,0,0,0
for i in numList:
    if i%2 == 0:
        sumEven = sumEven + i
        countEven = countEven + 1
    elif i%2 == 1:
        sumOdd = sumOdd + i
        countOdd = countOdd + 1
print("Sum of even numbers in the list is:           " + str(sumEven) + "\n" + "\nCount of even number in the list is:           " + str(countEven) + "\n" +
      "\nSum of odd numbers in the list is:            " + str(sumOdd) + "\n" + "\nCount of the odd numbers in the list is:       " + str(countOdd))
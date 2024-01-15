import math

loanAmount = 100000
monthlyInterestRate = 0.01
numYears = 7
numerator = loanAmount * monthlyInterestRate
denomerator = 1 - (1 / (math.pow(1 + monthlyInterestRate, (numYears * 12))))

monthlyPayment = numerator / denomerator

monthlyPayment1 = round(monthlyPayment, 2)
print('----')
print('Monthly payment is = ' + str(monthlyPayment) + " Or " + str(monthlyPayment1))

totalPayment = monthlyPayment * numYears * 12
print('----')
totalPayment1 = (round(totalPayment, 2))
print('Total Payment is = ' + str(totalPayment) + ' Or ' + str(totalPayment1))



#notes for anything

# Ex No 2 : # Swap commas and dot in a string

statement = "He is Ahmed, Ahmed lives in Cairo, Ahmed plays football."

statement = statement.replace('.','*')
statement = statement.replace(',','.')
statement = statement.replace('*',',')
print(statement)
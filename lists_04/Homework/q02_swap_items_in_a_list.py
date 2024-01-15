newList = [23, 65, 19, 90]
#size = len(newList)
temp = newList[1]
newList[1] = newList[3]
newList[3] = temp
print(newList)

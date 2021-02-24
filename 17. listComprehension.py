temps = [234, 256, 278, -9999, 289]
newtemp = [ temp/10 for temp in temps if temp != -9999]
print(newtemp)

combList = ['hello', 234, 'shyam', 456, 728]

newCombList = [ temp for temp in combList if type(temp) == int]
print(newCombList)

def retPostive(mixedlist):
    return [ i if i >= 0 else 0 for i in mixedlist ]

print(retPostive([-1, 0, -2, 1, 2, 3, 4]))

temps = [234, 256, 278, -9999, 289]
newtemp = [ temp/10  if temp != -9999 else 0 for temp in temps ]
print(newtemp)

def retSum(ilist):
    slist = [int(i) for i in ilist ]
    return sum(slist)

print(retSum(['1', '2', '3']))
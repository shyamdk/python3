def findmean(value):
    #if type(value == dict:
    if isinstance(value, dict):
        return sum(value.values()) / len(value)
    else:
        return sum(value)/len(value)

student_grades ={"Mary":10, "Ram":15, "Sita":20}
mon_temp = [10, 20, 30, 40]

print(findmean(student_grades))
print(findmean(mon_temp))

'''
You learned to check for one single condition:

x = 1
 
if x == 1:
    print("Yes")
else:
    print("No")
You can also check if two conditions are met at the same time using an and operator:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
That will return Yes since x == 1 and y ==1 are both True.

You can also check if one of two conditions are met using an or operator:

x = 1
y = 1
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
That will return Yes since at least one of the conditions is True. In this case x == 1 is True.
'''
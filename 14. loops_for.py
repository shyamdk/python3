mon_temp = [8.1, 8.5, 7.2]
for i in mon_temp:
    print(round(i))

for i in 'hello':
    print(i)

colors = [11, 34, 98, 43, 45, 54, 54]
for i in colors:
    if i > 50:
        print(i)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for x in colors:
    if type(x) == int and x > 50:
        print(x)

student_grades = {"mary": 30, "sam": 50, "ganesh": 60}
for grades in student_grades.items():
    print(grades)
'''
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
'''

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for key, value in phone_numbers.items():
    #print(key)
    print(value.replace("+", "00"))
    #print("{} : {}".format(i[0],i[1]))

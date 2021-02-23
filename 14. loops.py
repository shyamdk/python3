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
    if type(x) == int:
        print(x)
studentgrades = {"Mary": 8.1, "Sam": 8.8, "John": 7.5}
print(studentgrades.values())
print(studentgrades.keys())
print(studentgrades.items())
print(studentgrades.get("Mary"))
print(studentgrades.pop("Mary"))
print(studentgrades.items())
day_temperatures = {'morning': 33.0, 'afternoon':38.0, 'evening': 32.0}
print(day_temperatures)

print(studentgrades["Sam"])

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
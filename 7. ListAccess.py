serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])
print(serials[0], serials[2], serials[5])

workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)

print(serials[0]) #accessing a sepecific item
print(serials[3:5]) #access from first to until 2, thats is 0,1
print(serials[1:]) #access all elements from index 1
print(serials[:2]) #access first two elements? 

#negative indexiing
print(serials[-1])
print(serials[-2:])
print(serials[-5:])
print(serials[-5:-2])



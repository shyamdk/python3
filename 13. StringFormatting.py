name = input("Enter your name: ")
surname = input("Enter Surname: ")
age = input ("Enter your age:")
newage = float(age) + 6
#message = "Welcome %s!" %user_input
message = f"Hello {name} {surname}, it appears that your age is {age} and you will be {newage}"
print(message)

def printName(name):
    print(f"Hi {name}")

inputname = input("Please enter your name:")
printName(inputname.title())

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))
'''
A Python program can get user input via the input function:

The input function halts the execution of the program and gets text input from the user:

name = input("Enter your name: ")
The input function converts any input to a string, but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12
You can format strings with (works both on Python 2 and 3):

name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.

You can also format strings with:

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
Output: Hi Sim, you have 1.5 years of experience.
'''
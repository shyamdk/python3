'''
myfile = open("fruits.txt")
content = myfile.read()
print(content)  #cursor moves to the end of the file
myfile.close()
print(content)
'''

with open("files/fruits.txt") as myfile:  #close file not required, this is called context manager
    content = myfile.read()

print(content)

with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Cucumber\nTomoto\nGarlic")
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

with open("files/bear.txt") as myfile:  #close file not required, this is called context manager
    content = myfile.read()

print(content[:90])

def countChar(char, filepath):
    with open(filepath) as myfile:
        content = myfile.read()

    return content.count(char)

print(countChar('a', "files/bear.txt"))

with open("files/bear.txt") as rfile:  #close file not required, this is called context manager
    content = rfile.read()

with open("files/first.txt", "w") as wfile:  #close file not required, this is called context manager
    wfile.write(content[:100])

with open("files/first.txt") as cfile:  #close file not required, this is called context manager
    print(cfile.read())


#append and alos read, use a+ mode
with open("files/vegetables.txt", "a+") as myyfile:
    myyfile.write("\nOkra")
    myyfile.seek(0)
    content = myyfile.read()
print(content)

with open("files/data.txt", "a+") as datafile:
    datafile.seek(0)
    info = datafile.read()
    datafile.seek(0)
    datafile.write(info)
    datafile.seek(0)
    datafile.write(info)
    datafile.seek(0)
    inffo = datafile.read()

print(inffo)



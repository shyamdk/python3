import sys
import time
import os
#sys.builtin_module_names - gives all avalable modules
#print(sys.builtin_module_names)
#pip is used to install libraries. 
#update pip  - python -m pip install --upgrade pip.  (python and then scripts folder)
#add to path variable
# had to do all these using command prompt - did not work from bash


while True:
    if os.path.exists("files/vegetables.txt"):
        with open ("files/vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist")
    time.sleep(10)

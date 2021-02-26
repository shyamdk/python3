#pip is used to install libraries. 
#update pip  - python -m pip install --upgrade pip.  (python and then scripts folder)
#add to path variable
# had to do all these using command prompt - did not work from bash

#third pary modules get installaed under C:\Users\sdkrishn\AppData\Local\Programs\Python\Python38-32\Lib\site-packages
import time
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean())
    else:
        print("File does not exist")
    time.sleep(10)
'''
Builtin objects are all objects that are written inside the Python interpreter in C language.

Builtin modules contain builtins objects.

Some builtin objects are not immediately available in the global namespace. They are parts of a builtin module. To use those objects the module needs to be imported first. E.g.:

import time
time.sleep(5)
A list of all builtin modules can be printed out with:

import sys
sys.builtin_module_names
Standard libraries is a jargon that includes both builtin modules written in C and also modules written in Python.

Standard libraries written in Python reside in the Python installation directory as .py files. You can find their directory path with sys.prefix.

Packages are a collection of .py modules.

Third-party libraries are packages or modules written by third-party persons (not the Python core development team).

Third-party libraries can be installed from the terminal/command line:

Windows:

pip install pandas or use python -m pip install pandas if that doesn't work.

Mac and Linux:

pip3 install pandas or use python3 -m pip install pandas if that doesn't work.
'''
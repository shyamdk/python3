def areaRect (a, b = 8): #default value for b, all default parameters should be at the end
    return a * b

#print (areaRect(4, 5))
print (areaRect(b = 5, a = 6)) # argument order is not required, a and b when assinged here are called key word
print(areaRect(9))


#functions with arbitrary number of non key workd
def mean(*args):
    return sum(args)/ len(args) 

print(mean(10,20,30, 40))

def sortCaps(*args):
    args = [x.upper() for x in args]
    return sorted(args)

print(sortCaps("Shyam", "Ganesh"))

#function with arbritary no of key word arguments

def meana(**kwargs):
    return kwargs

print(meana(a=1,b=2,c=3))
def myFirstFunc(): 
    print("My First Function")

myFirstFunc()

def mySecondFunc (name):
    print ("Hi...",name)

mySecondFunc ("Uri")

def myThirdFunc(a,b):
    return(a+b)

a=1
b=2
print("The  sum of", a , " and ", b , " is: ",myThirdFunc(a,b))

# Built in functions

bl = bool(1)
st = "Uri"
integ = 1000
floaty = 1.1234

# Lists all methods that are possibly applied to data type/object

print (dir(bl))
print (dir(st))
print (dir(integ))
print (dir(floaty))

# print short documentation of any specific method of an applied item
help(st.upper)

st.u

# executes the pyton text between the quotes

s= 'print("Hello World")'
eval ('print("Hello World")')
eval (s)
exec (s)





# data type convert str() int() float() bool

a = 1

b = bool(a)
s = str(a)
f = float(a)

print (b,s,f)




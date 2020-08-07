def myFirstFunc (Name, Age=10):
    print("Name is:", Name)
    print("Age is:", Age)

"""
aaaaa


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Urik1234",
  database = "mmdemo"
)

print(mydb)


myFirstFunc(Name="aaabbb")
"""

xx = ("a","b","c")

print (xx)
print (type(xx))

name,age = "Uri", 62
f = __file__
print ("My name is; ",name, " and I'm ",age, "Old,","\n",name,age)
tup = ("t1","t2","t3")
name= "sjhsjhjsh"
print (tup)
if ((age>0) and (name != "Uri")):
    print (1)
    print (2)
else:
    print (3)
    print (4)
print(5)

i = 0
while (i<10):
    i = i+1
    print ('While ',i)
for j in range (10,100,5):
    print ('for ', j)    
for j in range(len(tup)):
    print (tup[j])
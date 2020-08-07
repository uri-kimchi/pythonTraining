import random

print ("Range as for loop")
myList = ("a","b","c","d","e","f")
# list of range
for joinedList in range(0,5,2):
    print (joinedList,myList[joinedList])

print ("Type conversion of ramge to list")
myList = list(range(1,20,3))
print (myList)

print ("Letters scan of String")

name = "Uri Kimchi"

for joinedList in name:
    print (joinedList)

print ("using Enumerate on string")
for joinedList in enumerate(name):
    print (joinedList)

print ("Creating a list from enumrate")
myList = list(enumerate(name))
print(myList)

print ("and now I reverse the list")
myList.reverse()
print(myList)

print("merge lists using ZIP function")
list1 =  (1,2,3,4)
list2 = (9,8,7,8)
list3 = ("a","b","c","ddd","out")
joinedList = list(zip(list1,list2,list3))
print ("-----a is in the list3",("a" in list3))
print ("-----A is in the list3",("A" in list3))
print("Joined List",joinedList)
for a1,a2,a3 in joinedList:
    print(a1,a2,a3)
for a1,a2,a3 in joinedList:
    print(a1,a2)
print (min(joinedList))


print("Some random numbers")

print ("Generate random numbers")
random.shuffle(myList)
for x in range (0,20,3):
    print(x,random.randint(10,100))

print ("Shuffle List")
print(myList)
random.shuffle(myList))
print(myList)
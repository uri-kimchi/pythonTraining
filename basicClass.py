class Man:
    def __init__(self, name, age, wgt):
#        super().__init__()
        self.name = name
        self.age = age
        self.wgt = wgt
        print ("Init Man")
    def getName (self):
        return (self.name)
    def getAge(self):
        return(self.age)
    def printMan(self):
        print ("The man is ",self.name," and he is:",self.age,"old.")

m = Man("David",30,100)

#print (m.__class__)
#print(m.getName())
m.printMan()

class Boy (Man):
    def setClass(self, schoolClass):
        self.schoolClass = schoolClass
    def printBoy(self):
        print ("The boy is ",self.name," and he is:",self.age,"old, learning in the ",self.schoolClass," class")
    def getAge(self):
        return super().getAge()*2
 
       
name_of_boy = input ("Enter the boy name please:")
b = Boy(name_of_boy,10,30)
b.setClass("Third")
b.printBoy()
b.printMan()

print("The boy age is: ", b.getAge())

# help(m)




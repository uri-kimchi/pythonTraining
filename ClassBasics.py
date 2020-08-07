import random


class PersonBasic():
    def __init__(self, name, salary, gender = "Unknown"):
        super().__init__()
        self.name = name
        self.id = random.randrange (1000000,9000000)
        self.salary = salary
        self.gender = gender

    def printPerson (self):
        print ("ID {} Name {} Salary {} Gender {}".format(self.id,self.name, self.salary,self.gender))


def ppp (px):
    px.printPerson()


p1 = PersonBasic (name = "Uri", salary = 1000)
p2 = PersonBasic (name = "Yaffa", salary = 1020, gender= "Female")
p3 = PersonBasic (name = "Shai", salary = 300)
p4 = PersonBasic (name = "Tal", salary = 500)

family = [p1,p2,p3,p4]
print ("P1 Type....: ",type(p1))

p1.printPerson()
p2.printPerson()
p3.printPerson()
p4.printPerson()


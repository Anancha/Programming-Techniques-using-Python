class Dog:
    def mytalk(self):
        print("Bark....Bark..")

class Crows:
    def mytalk(self):
        print("Caw....Caw..")

class Duck:
    def mytalk(self):
        print("Quack....Quack..")

class Owl:
    def myhoot(self):
        print("Hoot....Hoot..")

def myquack(object):
    #Pythonic code
    object.mytalk()

#M-1
myobj = Dog()
myquack(myobj)
myobj1 = Crows()
myquack(myobj1)
myobj2 = Duck()
myquack(myobj2)
myobj3 = Owl()
myquack(myobj3)
import time
class Tracks:
    def mobility(self):
        print("tracks")
class Vehicle:
    def __init__(self, objfromArg):
        self.typeOfMobility = objfromArg
    def thename(self):
        self.typeOfMobility.mobility()
#composition projects a class as a container able to store and use other objects
tracked = Vehicle(Tracks())

tracked.thename()#tracks
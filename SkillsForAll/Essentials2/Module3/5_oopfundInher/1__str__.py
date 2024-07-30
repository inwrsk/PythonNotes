#to print object
class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

sun = Star("Sun", "Milky Way")
print(sun)#<__main__.Star object at 0x000001A5F7F6BF40>
print(sun.__str__)#<method-wrapper '__str__' of Star object at 0x000001A5F7F6BF40>

class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
    def __str__(self):
        return self.name + ' in ' + self.galaxy
    
sun = Star("Sun", "Andreomeda")
print(sun)#Sun in Andreomeda
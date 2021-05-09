class apollo:
    
    def __init__(self,param): #""" object initialization constructor """
        self.dest=param

    def fly(self):
        print("spaceship flying..")
    
    def destination(self):
        print("destination is: "+self.dest)

obj1=apollo('moon')

obj1.fly()
obj1.destination()

obj2=apollo('mars')
# obj2.dest='mars'

obj2.fly()
obj2.destination()


class example:
    def __new__(self): #""" object creation constructor """
        return 'studytonight'

obj3=example()
print(type(obj3))
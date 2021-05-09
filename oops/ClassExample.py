class shobhit:
    name='shobhit jaiswal'
    addrs='Faizabad'
    aged=24
    def address(self):
        print(self.addrs);

    def age(self):
        print('My name is '+ self.name + ' My age is '+ str(self.aged));

obj1=shobhit()
obj2=shobhit()

obj1.name='rachit kumar'
obj1.addrs='delhi'
obj1.aged=25
obj1.address()
obj1.age()


obj2.address()
obj2.age()
